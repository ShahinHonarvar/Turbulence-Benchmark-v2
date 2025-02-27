def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == 'Q':
            output_string += 'QI'
        output_string += input_string[i]
    return output_string