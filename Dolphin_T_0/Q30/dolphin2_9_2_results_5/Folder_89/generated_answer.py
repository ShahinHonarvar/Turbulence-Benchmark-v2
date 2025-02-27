def insert_before_character(input_string):
    result_string = ''
    for character in input_string:
        if character == ' ':
            result_string = result_string + 'W' + character
        else:
            result_string = result_string + character
    return result_string