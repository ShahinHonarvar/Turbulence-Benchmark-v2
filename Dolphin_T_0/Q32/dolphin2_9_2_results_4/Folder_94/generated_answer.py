def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char + ('5' if char == ' ' else '')
    return new_string