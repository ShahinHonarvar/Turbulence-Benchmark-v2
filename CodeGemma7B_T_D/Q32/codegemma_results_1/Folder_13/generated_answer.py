def insert_after_character(str):
    new_string = ''
    for char in str:
        if char == 'x':
            new_string += char + 'N'
        else:
            new_string += char
    return new_string