def insert_after_character(s):
    new_s = ''
    for c in s:
        if c == 'M':
            new_s += 'f'
        new_s += c
    return new_s