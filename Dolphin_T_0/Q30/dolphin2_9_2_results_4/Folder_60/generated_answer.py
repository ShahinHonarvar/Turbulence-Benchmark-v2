def insert_before_character(input_str):
    output_str = ''
    for char in input_str:
        if char == 'C':
            output_str += 'P' + char
        else:
            output_str += char
    return output_str