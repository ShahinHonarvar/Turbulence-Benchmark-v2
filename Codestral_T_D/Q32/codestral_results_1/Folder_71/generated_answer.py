def insert_after_character(input_string):
    result_string = ''
    for char in input_string:
        result_string += char
        if char == '2':
            result_string += 'S'
    return result_string