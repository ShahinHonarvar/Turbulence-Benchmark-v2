def insert_before_character(s):
    result = []
    for char in s:
        if char == 'O':
            result.append('o')
        result.append(char)
    return ''.join(result)