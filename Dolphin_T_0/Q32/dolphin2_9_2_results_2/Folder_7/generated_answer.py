def insert_after_character(input_string):
    new_string = ''
    for i in input_string:
        new_string += i
        if i == ' ':
            new_string += 'H'
    return new_string