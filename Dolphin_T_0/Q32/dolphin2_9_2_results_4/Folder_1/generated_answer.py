def insert_after_character(string):
    new_string = ''
    for i in range(len(string)):
        new_string += string[i]
        if string[i] == 'U':
            new_string += 'T'
    return new_string