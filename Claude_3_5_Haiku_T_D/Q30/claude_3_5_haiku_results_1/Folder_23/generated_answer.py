def insert_before_character(s):
    result = []
    for char in s:
        if char == 'b':
            result.append('y')
        result.append(char)
    return ''.join(result)