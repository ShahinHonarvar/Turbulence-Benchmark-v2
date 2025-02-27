def insert_after_character(input_string):
    output_string = ''
    for i in input_string:
        if i == 'O':
            output_string = output_string + 'Od'
        else:
            output_string = output_string + i
    return output_string