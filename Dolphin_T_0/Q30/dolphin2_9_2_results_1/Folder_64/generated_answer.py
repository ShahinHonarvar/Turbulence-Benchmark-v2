def insert_before_character(string):
    new_string = ''
    for char in string:
        new_string += 'u' + char if char == 'u' else char
    return new_string