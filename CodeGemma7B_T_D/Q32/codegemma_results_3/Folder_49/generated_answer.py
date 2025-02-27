def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'i':
            new_str += char + 'i'
        else:
            new_str += char
    return new_str