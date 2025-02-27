def insert_before_character(str):
    new_str = ''
    for c in str:
        if c == 'I':
            new_str += ' ' + c
        else:
            new_str += c
    return new_str