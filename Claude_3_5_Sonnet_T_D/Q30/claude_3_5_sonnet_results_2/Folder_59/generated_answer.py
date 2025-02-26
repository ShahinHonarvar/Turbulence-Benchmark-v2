def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'o':
            result += '0'
        result += char
    return result