def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == '6':
            output_string += '69'
        else:
            output_string += input_string[i]
    return output_string