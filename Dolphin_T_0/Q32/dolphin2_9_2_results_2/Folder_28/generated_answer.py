def insert_after_character(s):
    new_s = ''
    for c in s:
        new_s += c
        if c == 'r':
            new_s += '1'
    return new_s