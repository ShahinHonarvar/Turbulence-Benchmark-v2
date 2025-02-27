def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        if char == 'U':
            output_string += char + 'T'
        else:
            output_string += char
    return output_string