def insert_after_character(input_string):
    new_string = ''
    for i in range(len(input_string)):
        new_string += input_string[i]
        if input_string[i] == '0':
            new_string += '4'
    return new_string