def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'A':
            result += 'H'
        result += char
    return result