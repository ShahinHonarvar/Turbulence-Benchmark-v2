def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'E':
            result += 'E'
        result += char
    return result