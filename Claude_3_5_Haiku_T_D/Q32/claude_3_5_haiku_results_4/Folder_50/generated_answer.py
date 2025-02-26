def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == 't':
            result.append('u')
    return ''.join(result)