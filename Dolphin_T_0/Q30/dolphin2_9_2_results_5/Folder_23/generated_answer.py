def insert_before_character(input_string):
    output_string = ''
    for i in input_string:
        if i == 'b':
            output_string += 'y' + i
        else:
            output_string += i
    return output_string