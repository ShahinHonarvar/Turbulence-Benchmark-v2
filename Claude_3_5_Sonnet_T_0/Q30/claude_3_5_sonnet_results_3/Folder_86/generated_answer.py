def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'O':
            result += 'Q'
        result += char
    return result