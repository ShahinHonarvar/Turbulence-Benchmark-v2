def insert_before_character(string):
    new_string = ''
    for i in string:
        if i == ' ':
            new_string += ' '
        new_string += i
    return new_string