def insert_before_character(string):
    output_string = ''
    for char in string:
        if char == 'T':
            output_string += 'V' + char
        else:
            output_string += char
    return output_string