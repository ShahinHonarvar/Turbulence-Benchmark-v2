def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'o':
            result += 'O'
        result += char
    return result