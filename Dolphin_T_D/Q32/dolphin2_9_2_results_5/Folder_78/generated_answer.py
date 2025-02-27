def insert_after_character(string):
    new_string = ''
    for i in string:
        new_string += i
        if i == 'H':
            new_string += 's'
    return new_string