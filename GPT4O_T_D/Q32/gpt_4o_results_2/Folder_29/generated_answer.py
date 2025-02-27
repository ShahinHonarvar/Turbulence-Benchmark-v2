def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'N':
            result.append('z')
    return ''.join(result)