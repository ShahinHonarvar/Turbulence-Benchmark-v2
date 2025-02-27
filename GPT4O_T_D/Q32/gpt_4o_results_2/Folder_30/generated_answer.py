def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == '4':
            result.append('F')
    return ''.join(result)