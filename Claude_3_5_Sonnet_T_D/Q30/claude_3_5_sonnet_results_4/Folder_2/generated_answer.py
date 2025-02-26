def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'C':
            result += 'Z'
        result += char
    return result