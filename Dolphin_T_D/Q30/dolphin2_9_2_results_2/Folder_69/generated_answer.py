def insert_before_character(a_string):
    new_string = ''
    for char in a_string:
        new_string += char
        if char == ' ':
            new_string += 'P'
    return new_string