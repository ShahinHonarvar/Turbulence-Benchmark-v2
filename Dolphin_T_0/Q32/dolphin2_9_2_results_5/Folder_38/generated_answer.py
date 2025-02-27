def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'X':
            output_string += '6'
    return output_string