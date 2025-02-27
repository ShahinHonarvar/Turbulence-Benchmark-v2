def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'A':
            new_string += 'A'
        new_string += char
    return new_string