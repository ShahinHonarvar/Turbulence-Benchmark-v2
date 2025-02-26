def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'O':
            result += 'd'
        result += char
    return result