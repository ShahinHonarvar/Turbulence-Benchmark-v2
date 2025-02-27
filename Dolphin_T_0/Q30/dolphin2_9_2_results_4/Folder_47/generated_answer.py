def insert_before_character(string):
    new_string = ''
    for char in string:
        if char.upper() == 'E':
            new_string += 'f' + char
        else:
            new_string += char
    return new_string