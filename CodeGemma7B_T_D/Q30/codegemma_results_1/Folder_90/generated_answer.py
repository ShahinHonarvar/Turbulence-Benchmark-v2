def insert_before_character(string):
    result = []
    for char in string:
        if char == 'U':
            result.append('F')
        result.append(char)
    return ''.join(result)