def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == '6':
            new_str += char + 'W'
        else:
            new_str += char
    return new_str