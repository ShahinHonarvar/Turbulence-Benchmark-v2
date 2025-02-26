def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'H':
            result += 's'
        result += char
    return result