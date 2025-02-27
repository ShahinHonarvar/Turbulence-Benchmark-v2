def insert_before_character(s):
    new_str = ''
    for c in s:
        if c == 'U':
            new_str += 'aU'
        else:
            new_str += c
    return new_str