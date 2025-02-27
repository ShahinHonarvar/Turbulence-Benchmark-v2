def insert_after_character(my_str):
    new_str = ''
    for char in my_str:
        if char == 'O':
            new_str += char + 'j'
        else:
            new_str += char
    return new_str