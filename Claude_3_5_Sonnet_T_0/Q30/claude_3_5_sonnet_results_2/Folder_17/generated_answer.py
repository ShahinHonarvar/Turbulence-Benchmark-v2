def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'Q':
            result += 'I'
        result += char
    return result