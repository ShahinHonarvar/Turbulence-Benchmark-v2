def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'U':
            new_string += char + 'U'
        else:
            new_string += char
    return new_string