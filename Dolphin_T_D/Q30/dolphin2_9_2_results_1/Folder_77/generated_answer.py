def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == '9':
            new_string += 'h' + char
        else:
            new_string += char
    return new_string