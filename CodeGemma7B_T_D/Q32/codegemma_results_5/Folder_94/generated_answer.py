def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == ' ':
            new_string += char + '5'
        else:
            new_string += char
    return new_string