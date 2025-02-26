def insert_before_character(s):
    result = []
    for char in s:
        if char == 'g':
            result.append('t')
        result.append(char)
    return ''.join(result)