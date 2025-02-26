def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'T':
            result += ' '
        result += char
    return result