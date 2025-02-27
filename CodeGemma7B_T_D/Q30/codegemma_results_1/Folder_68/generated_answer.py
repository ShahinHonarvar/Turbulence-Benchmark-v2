def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'i':
            new_str += '0i'
        else:
            new_str += char
    return new_str