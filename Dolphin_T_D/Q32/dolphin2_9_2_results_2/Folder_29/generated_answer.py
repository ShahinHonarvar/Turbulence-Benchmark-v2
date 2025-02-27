def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'N':
            output_string += 'z'
    return output_string