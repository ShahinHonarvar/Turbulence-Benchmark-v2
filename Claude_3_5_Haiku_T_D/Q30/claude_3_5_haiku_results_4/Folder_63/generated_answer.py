def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '5':
            result += 'R5'
        else:
            result += char
    return result