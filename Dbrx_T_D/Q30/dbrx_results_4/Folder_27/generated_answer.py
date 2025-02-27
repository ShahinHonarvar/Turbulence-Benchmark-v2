def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'N':
            result += 'jN'
        else:
            result += char
    return result