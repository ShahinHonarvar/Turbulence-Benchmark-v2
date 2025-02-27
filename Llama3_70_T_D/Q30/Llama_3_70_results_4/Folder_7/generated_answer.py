def insert_before_character(input_string):
    result_string = ''
    for char in input_string:
        if char == ' ':
            result_string += 'H'
        result_string += char
    return result_string