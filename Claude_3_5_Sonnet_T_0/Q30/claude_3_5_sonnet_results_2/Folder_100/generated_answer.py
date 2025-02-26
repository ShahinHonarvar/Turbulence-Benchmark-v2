def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '0':
            result += ' '
        result += char
    return result