def insert_after_character(string):
    new_string = ''
    for i in string:
        new_string += i
        if i == 'I':
            new_string += ' '
    return new_string