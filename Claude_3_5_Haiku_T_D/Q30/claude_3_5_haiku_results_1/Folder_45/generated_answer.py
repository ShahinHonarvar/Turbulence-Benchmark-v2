def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'O':
            result += 'OO'
        else:
            result += char
    return result