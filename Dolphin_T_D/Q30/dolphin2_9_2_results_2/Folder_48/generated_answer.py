def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'S':
            new_string += 'U' + char
        else:
            new_string += char
    return new_string