def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'x':
            new_string += 'N'
    return new_string