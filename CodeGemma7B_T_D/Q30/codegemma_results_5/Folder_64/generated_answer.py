def insert_before_character(string):
    new_string = ''
    for char in string:
        if char == 'u':
            new_string += 'u'
        new_string += char
    return new_string