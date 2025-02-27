def insert_before_character(input_string):
    result = ''
    for i, char in enumerate(input_string):
        if char == 'm':
            result += 'Q'
        result += char
    return result