def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'B':
            result += 'N'
        result += char
    return result