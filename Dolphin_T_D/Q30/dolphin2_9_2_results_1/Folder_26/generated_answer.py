def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'r':
            new_string += 'w'
        new_string += char
    return new_string