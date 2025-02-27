def insert_after_character(s):
    new_s = ''
    for c in s:
        new_s += c
        if c == 'S':
            new_s += 'U'
    return new_s