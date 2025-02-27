def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == '0':
            new_string += 'H0'
        else:
            new_string += char
    return new_string