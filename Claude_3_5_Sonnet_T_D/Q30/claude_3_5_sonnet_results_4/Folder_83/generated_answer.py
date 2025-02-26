def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'E':
            result += 'e'
        result += char
    return result