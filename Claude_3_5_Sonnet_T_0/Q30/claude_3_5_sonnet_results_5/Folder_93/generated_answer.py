def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'Y':
            result += '4'
        result += char
    return result