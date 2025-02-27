def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'j':
            result += '1j'
        else:
            result += char
    return result