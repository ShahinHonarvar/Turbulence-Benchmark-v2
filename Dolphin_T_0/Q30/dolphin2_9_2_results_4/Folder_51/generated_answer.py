def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'o':
            new_string += 'O' + char
        else:
            new_string += char
    return new_string