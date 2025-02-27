def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'C':
            new_str += char + 'Z'
        else:
            new_str += char
    return new_str