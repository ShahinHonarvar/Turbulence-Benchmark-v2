def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == '0':
            new_string += char + ' '
        else:
            new_string += char
    return new_string