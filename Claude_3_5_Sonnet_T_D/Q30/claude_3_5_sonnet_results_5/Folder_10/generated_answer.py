def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'j':
            result += 'v'
        result += char
    return result