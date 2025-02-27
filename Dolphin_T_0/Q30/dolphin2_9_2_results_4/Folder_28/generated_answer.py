def insert_before_character(input_string):
    new_string = ''
    for i in range(len(input_string)):
        if input_string[i] == 'r' and i != 0:
            new_string += '1' + input_string[i]
        else:
            new_string += input_string[i]
    return new_string