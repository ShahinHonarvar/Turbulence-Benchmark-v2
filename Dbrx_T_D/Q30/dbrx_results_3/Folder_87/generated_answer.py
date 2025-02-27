def insert_before_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == 'm':
            output_string += 'N' + input_string[i]
        else:
            output_string += input_string[i]
    return output_string