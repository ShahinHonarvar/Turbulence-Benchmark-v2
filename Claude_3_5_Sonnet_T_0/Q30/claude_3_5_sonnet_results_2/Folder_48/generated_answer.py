def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'S':
            result += 'U'
        result += char
    return result