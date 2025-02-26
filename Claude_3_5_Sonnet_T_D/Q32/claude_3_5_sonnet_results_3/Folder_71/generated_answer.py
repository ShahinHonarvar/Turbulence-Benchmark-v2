def insert_after_character(input_string):
    result = ''
    for char in input_string:
        result += char
        if char == '2':
            result += 'S'
    return result