def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == '0':
            new_str += char + '4'
        else:
            new_str += char
    return new_str