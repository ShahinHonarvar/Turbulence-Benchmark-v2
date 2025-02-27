def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == '2':
            output_string += '2S'
        else:
            output_string += input_string[i]
    return output_string