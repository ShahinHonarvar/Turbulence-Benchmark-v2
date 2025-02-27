def insert_after_character(str):
    new_str = ''
    for c in str:
        if c == 'A':
            new_str += c + 'A'
        else:
            new_str += c
    return new_str