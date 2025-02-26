def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'R':
            result += 'V'
        result += char
    return result