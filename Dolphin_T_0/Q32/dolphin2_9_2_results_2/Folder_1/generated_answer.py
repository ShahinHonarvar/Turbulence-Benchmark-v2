def insert_after_character(string):
    new_string = ''
    for i in string:
        new_string += i
        if i == 'U':
            new_string += 'T'
    return new_string