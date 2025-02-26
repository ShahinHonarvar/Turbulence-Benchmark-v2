def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 's':
            result += 'w'
        result += char
    return result