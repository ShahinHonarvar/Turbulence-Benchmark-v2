def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'm':
            new_string += char + 'Q'
        else:
            new_string += char
    return new_string