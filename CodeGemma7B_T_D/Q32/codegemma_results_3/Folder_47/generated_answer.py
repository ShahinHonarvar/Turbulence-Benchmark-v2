def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'E':
            new_string += char + 'f'
        else:
            new_string += char
    return new_string