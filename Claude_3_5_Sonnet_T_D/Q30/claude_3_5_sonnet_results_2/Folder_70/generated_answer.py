def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'P':
            result += 'V'
        result += char
    return result