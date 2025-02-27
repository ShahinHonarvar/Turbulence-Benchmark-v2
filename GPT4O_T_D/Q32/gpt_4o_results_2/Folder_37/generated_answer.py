def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'U':
            result.append('a')
    return ''.join(result)