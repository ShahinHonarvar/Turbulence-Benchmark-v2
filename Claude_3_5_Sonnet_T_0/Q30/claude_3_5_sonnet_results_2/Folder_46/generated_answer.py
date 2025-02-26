def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '6':
            result += 'W'
        result += char
    return result