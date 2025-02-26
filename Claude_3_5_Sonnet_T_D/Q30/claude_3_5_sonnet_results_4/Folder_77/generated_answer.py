def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '9':
            result += 'h'
        result += char
    return result