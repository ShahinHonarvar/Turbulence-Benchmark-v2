def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'O':
            new_string += char + 'd'
        else:
            new_string += char
    return new_string