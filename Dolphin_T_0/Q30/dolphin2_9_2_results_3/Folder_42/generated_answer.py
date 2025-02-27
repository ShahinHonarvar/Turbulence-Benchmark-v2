def insert_before_character(input_string):
    output_string = ''
    for char in input_string:
        if char == 'O':
            output_string += 'j' + char
        else:
            output_string += char
    return output_string