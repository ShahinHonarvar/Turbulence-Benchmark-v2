def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'O':
            result += 'O'
        result += char
    return result