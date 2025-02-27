def insert_after_character(input_string):
    result = ''
    for character in input_string:
        result += character
        if character == 'i':
            result += 'I'
    return result