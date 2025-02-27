def insert_after_character(s):
    new_str = ''
    for c in s:
        if c == ' ':
            new_str += c + 'K'
        else:
            new_str += c
    return new_str