def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == 'O':
            new_string += 'o'
    return new_string