def insert_after_character(s):
    s = s + ' '
    new_s = ''
    for c in s:
        if c == 'g':
            new_s = new_s + c + 'M'
        else:
            new_s = new_s + c
    return new_s.rstrip()