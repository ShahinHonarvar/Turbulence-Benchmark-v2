def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'r':
            new_string += char + '1'
        else:
            new_string += char
    return new_string