def insert_before_character(string):
    result = []
    for char in string:
        if char == '9':
            result.append('h')
        result.append(char)
    return ''.join(result)