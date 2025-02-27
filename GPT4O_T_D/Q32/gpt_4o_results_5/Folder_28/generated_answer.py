def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'r':
            result.append('1')
    return ''.join(result)