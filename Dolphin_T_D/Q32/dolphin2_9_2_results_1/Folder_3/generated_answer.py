def insert_after_character(input_str):
    output_str = ''
    for char in input_str:
        output_str += char
        if char == '0':
            output_str += 'H'
    return output_str