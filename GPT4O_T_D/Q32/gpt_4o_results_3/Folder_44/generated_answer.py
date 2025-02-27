def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'g':
            result.append('M')
    return ''.join(result)