def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == 'U':
            result.append('q')
    return ''.join(result)