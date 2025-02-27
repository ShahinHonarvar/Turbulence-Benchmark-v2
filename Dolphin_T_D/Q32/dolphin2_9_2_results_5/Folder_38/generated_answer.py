def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'X':
            new_string += '6'
    return new_string