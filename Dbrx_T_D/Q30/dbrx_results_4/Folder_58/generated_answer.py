def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'F':
            result += 'o' + char
        else:
            result += char
    return result