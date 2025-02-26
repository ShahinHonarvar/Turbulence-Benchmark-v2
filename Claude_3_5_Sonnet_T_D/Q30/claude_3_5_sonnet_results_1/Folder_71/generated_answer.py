def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '2':
            result += 'S'
        result += char
    return result