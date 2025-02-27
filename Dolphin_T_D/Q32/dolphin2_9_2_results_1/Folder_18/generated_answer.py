def insert_after_character(s):
    new_s = ''
    for c in s:
        new_s += c
        if c == 'K':
            new_s += 'l'
    return new_s