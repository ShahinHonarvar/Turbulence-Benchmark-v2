def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'N':
            new_string += 'j' + char
        else:
            new_string += char
    return new_string