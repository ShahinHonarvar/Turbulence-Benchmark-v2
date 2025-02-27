def insert_before_character(s):
    new_s = ''
    for c in s:
        new_s += c
        if c == '5':
            new_s += 'R'
    return new_s