def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'k':
            result.append('k')
    return ''.join(result)