def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == '4':
            result += 'F4'
        else:
            result += char
    return result