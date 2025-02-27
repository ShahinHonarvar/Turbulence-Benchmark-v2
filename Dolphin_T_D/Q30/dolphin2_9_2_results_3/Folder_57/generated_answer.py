def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 's':
            new_string += 'w' + char
        else:
            new_string += char
    return new_string