def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        output_string += input_string[i]
        if input_string[i] == 'c':
            output_string += 'G'
    return output_string