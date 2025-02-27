def insert_before_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'O':
            new_string += 'O'
    return new_string