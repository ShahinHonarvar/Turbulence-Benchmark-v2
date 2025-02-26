def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'F':
            result += 'o'
        result += char
    return result