def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'm':
            new_str += 'N' + char
        else:
            new_str += char
    return new_str