def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'g':
            result += 't'
        result += char
    return result