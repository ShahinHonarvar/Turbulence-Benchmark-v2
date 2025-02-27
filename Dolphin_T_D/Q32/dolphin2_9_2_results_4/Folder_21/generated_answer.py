def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char
        if char == ' ':
            new_string += 'K'
    return new_string