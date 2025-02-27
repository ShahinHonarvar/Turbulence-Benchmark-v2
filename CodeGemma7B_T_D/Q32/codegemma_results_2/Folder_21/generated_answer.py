def insert_after_character(string):
    new_string = ''
    for char in string:
        if char != 'K':
            new_string += char
        if char == ' ':
            new_string += char + 'K'
    return new_string