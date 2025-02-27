def insert_after_character(s):
    new_s = ''
    for c in s:
        if c == 'O':
            new_s += c + 'd'
        else:
            new_s += c
    return new_s