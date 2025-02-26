def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'm':
            result += 'Q'
        result += char
    return result