def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'H':
            result += 'n'
        result += char
    return result