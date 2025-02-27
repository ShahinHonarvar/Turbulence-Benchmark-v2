def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'A':
            output_string += 'H'
    return output_string