def insert_after_character(string):
    new_string = ''
    for i in range(len(string)):
        new_string += string[i]
        if string[i] == '6':
            new_string += '9'
    return new_string