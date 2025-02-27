def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 't':
            new_string += 'G' + char
        else:
            new_string += char
    return new_string