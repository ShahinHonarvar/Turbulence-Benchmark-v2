def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        if char == '0':
            output_string += char + 'H'
        else:
            output_string += char
    return output_string