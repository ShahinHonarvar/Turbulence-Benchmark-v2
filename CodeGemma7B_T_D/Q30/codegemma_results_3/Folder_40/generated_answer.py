def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'e':
            new_string += 'e' + char
        else:
            new_string += char
    return new_string