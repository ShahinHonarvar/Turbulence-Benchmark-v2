def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'C':
            new_string += 'Z' + char
        else:
            new_string += char
    return new_string