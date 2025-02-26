def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'I':
            result += 'II'
        else:
            result += char
    return result