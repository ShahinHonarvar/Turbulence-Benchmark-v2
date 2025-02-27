def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'e':
            new_string += char + 'E'
        else:
            new_string += char
    return new_string