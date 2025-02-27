def insert_after_character(s):
    new_s = ''
    for c in s:
        new_s += c
        if c == 'E':
            new_s += 'T'
    return new_s