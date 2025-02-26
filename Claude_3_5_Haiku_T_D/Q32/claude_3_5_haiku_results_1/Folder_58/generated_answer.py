def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'F':
            result.append('o')
    return ''.join(result)