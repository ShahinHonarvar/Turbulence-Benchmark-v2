def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'a':
            new_string += char + 'n'
        else:
            new_string += char
    return new_string