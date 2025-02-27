def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'o':
            new_str += char + 'o'
        else:
            new_str += char
    return new_str