def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'F':
            result += 'm'
        result += char
    return result