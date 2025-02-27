def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'U':
            new_string += 'F'
    return new_string