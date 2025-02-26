def insert_after_character(string):
    result = []
    for char in string:
        result.append(char)
        if char == 'N':
            result.append('z')
    return ''.join(result)