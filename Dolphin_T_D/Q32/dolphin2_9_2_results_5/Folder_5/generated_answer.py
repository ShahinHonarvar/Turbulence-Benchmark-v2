def insert_after_character(input_string):
    new_string = ''
    for i in range(len(input_string)):
        if input_string[i] == 'c':
            new_string += input_string[i] + 'G'
        else:
            new_string += input_string[i]
    return new_string