def insert_before_character(s):
    result = []
    for char in s:
        if char == 'o':
            result.append('O')
        result.append(char)
    return ''.join(result)