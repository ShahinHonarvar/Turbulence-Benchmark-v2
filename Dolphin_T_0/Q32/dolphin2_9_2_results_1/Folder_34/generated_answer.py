def insert_after_character(s):
    new_s = ''
    for ch in s:
        new_s += ch
        if ch == 'A':
            new_s += 'a'
    return new_s