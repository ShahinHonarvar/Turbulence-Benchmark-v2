def insert_after_character(string):
    new_string = ''
    for char in string:
        new_string += char + 'I' if char == 'I' else char
    return new_string