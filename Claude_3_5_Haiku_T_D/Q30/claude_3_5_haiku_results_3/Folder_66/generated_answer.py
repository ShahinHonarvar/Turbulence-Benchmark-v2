def insert_before_character(s):
    result = []
    for char in s:
        if char == 'k':
            result.append('k')
        result.append(char)
    return ''.join(result)