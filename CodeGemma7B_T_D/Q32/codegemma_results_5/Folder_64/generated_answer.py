def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'u':
            new_string += char + 'u'
        else:
            new_string += char
    return new_string