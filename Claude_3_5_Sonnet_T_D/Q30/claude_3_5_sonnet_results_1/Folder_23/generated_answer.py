def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'b':
            result += 'y'
        result += char
    return result