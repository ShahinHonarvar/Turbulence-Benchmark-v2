def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'i':
            result += 'I'
        result += char
    return result