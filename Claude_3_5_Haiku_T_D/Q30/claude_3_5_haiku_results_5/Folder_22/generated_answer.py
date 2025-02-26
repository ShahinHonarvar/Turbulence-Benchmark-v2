def insert_before_character(s):
    result = []
    for char in s:
        if char == 'U':
            result.append('U')
        result.append(char)
    return ''.join(result)