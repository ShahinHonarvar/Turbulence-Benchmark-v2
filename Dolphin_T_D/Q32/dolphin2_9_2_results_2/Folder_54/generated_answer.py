def insert_after_character(string):
    new_string = ''
    for i in string:
        if i == 'M':
            new_string += 'Mf'
        else:
            new_string += i
    return new_string