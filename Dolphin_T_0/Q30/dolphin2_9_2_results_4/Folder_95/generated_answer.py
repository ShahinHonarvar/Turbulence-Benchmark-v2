def insert_before_character(input_string):
    new_string = ''
    for i in range(len(input_string) - 1):
        new_string += input_string[i]
        if input_string[i] == 'j':
            new_string += 'q'
    new_string += input_string[-1]
    return new_string