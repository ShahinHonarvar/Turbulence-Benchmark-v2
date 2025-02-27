def insert_before_character(input_text):
    output_text = ''
    for char in input_text:
        if char == 'A':
            output_text += 'A' + char
        else:
            output_text += char
    return output_text