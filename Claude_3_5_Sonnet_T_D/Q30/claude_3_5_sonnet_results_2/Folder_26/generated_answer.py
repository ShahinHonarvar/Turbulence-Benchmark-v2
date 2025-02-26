def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'r':
            result += 'w'
        result += char
    return result