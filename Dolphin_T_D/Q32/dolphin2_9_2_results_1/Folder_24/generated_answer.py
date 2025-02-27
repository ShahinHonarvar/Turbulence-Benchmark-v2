def insert_after_character(input_string):
    output_string = ''
    for i in input_string:
        output_string += i
        if i == '0':
            output_string += '4'
    return output_string