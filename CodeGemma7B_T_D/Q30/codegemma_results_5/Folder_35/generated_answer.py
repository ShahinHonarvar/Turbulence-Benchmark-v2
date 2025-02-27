def insert_before_character(str):
    new_str = ''
    for c in str:
        if c == '9':
            new_str += 'M' + c
        else:
            new_str += c
    return new_str