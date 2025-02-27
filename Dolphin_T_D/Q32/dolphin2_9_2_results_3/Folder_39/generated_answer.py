def insert_after_character(s):
    new_s = ''
    for ch in s:
        new_s += ch
        if ch == 'm':
            new_s += 'Q'
    return new_s