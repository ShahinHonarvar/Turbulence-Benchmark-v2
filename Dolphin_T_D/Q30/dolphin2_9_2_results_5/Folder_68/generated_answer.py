def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'i':
            new_string += '0i'
        else:
            new_string += char
    return new_string