def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'u':
            result.append('U')
    return ''.join(result)