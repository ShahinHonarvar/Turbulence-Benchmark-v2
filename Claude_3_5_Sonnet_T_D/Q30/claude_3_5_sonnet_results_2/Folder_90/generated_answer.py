def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'U':
            result += 'F'
        result += char
    return result