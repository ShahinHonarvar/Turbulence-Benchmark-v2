def insert_before_character(string):
    new_string = ''
    for i in string:
        if i == 'C':
            new_string += 'P' + i
        else:
            new_string += i
    return new_string