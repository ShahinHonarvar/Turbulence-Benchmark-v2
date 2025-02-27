def insert_after_character(s):
    new_str = ''
    for ch in s:
        new_str += ch
        if ch == 'i':
            new_str += 'I'
    return new_str