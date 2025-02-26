def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'X':
            result += '6'
        result += char
    return result