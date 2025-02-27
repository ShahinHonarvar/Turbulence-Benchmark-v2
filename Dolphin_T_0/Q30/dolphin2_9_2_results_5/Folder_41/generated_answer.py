def insert_before_character(input_string):
    result_string = ''
    for char in input_string:
        if char == 'O':
            result_string += 'o' + char
        else:
            result_string += char
    return result_string