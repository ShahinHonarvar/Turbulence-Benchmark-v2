def insert_after_character(input_string):
    output_string = ''
    for char in input_string:
        output_string += char
        if char == 'a':
            output_string += 'a'
    return output_string