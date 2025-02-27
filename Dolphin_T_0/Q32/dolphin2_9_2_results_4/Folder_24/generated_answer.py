def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        output_string += input_string[i]
        if input_string[i] == '0':
            output_string += '4'
    return output_string