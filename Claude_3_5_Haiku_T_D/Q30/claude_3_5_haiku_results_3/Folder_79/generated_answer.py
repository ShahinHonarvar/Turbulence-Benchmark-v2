def insert_before_character(s):
    result = []
    for char in s:
        if char == 'E':
            result.append('E')
        result.append(char)
    return ''.join(result)