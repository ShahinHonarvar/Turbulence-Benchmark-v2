def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'j':
            result += '1'
        result += char
    return result