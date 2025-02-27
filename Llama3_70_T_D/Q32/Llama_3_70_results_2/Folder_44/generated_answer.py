def insert_after_character(input_string):
    result_string = ''
    for char in input_string:
        result_string += char
        if char == 'g':
            result_string += 'M'
    return result_string