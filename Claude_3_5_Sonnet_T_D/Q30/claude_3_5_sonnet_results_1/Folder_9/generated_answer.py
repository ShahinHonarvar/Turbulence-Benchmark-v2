def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'e':
            result += 'E'
        result += char
    return result