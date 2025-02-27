def insert_before_character(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] == 'E' and i > 0:
            new_string += 'E'
        new_string += string[i]
    return new_string