def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'R':
            new_string += 'V' + char
        else:
            new_string += char
    return new_string