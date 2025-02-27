def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'A':
            new_str += char + 'H'
        else:
            new_str += char
    return new_str