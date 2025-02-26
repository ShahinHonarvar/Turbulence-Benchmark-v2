def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '4':
            result += 'F'
        result += char
    return result