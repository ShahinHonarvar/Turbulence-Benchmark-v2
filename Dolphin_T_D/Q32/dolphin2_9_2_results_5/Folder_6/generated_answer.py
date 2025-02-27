def insert_after_character(input_string):
    output_string = ''
    for i in range(len(input_string)):
        if input_string[i] == 'X':
            output_string += input_string[i] + 'u'
        else:
            output_string += input_string[i]
    return output_string