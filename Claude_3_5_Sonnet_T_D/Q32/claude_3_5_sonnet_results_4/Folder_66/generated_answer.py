def insert_after_character(input_string):
    result = ''
    for char in input_string:
        result += char
        if char == 'k':
            result += 'k'
    return result