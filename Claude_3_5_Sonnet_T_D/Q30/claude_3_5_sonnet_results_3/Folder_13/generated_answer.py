def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'x':
            result += 'N'
        result += char
    return result