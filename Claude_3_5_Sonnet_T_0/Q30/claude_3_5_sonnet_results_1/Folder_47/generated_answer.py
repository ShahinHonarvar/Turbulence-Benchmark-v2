def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'E':
            result += 'f'
        result += char
    return result