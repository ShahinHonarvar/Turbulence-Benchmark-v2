def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == 'm':
            result.append('N')
    return ''.join(result)