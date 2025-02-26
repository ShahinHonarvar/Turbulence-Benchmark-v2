def insert_after_character(input_string):
    result = []
    for char in input_string:
        result.append(char)
        if char == 'K':
            result.append('l')
    return ''.join(result)