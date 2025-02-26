def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '9':
            result += 'M'
        result += char
    return result