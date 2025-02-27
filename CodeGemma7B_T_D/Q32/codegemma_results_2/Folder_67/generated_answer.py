def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'j':
            new_string += char + '1'
        else:
            new_string += char
    return new_string