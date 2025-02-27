def insert_after_character(input_string):
    output_string = ''
    for i in input_string:
        output_string += i
        if i == 'T':
            output_string += 'V'
    return output_string