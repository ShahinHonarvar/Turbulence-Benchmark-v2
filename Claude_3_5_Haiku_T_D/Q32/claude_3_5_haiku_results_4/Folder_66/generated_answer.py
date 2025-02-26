def insert_after_character(input_string):
    result = []
    for char in input_string:
        result.append(char)
        if char == 'k':
            result.append('k')
    return ''.join(result)