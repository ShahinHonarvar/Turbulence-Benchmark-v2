def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'a':
            new_string += 'A'
    return new_string