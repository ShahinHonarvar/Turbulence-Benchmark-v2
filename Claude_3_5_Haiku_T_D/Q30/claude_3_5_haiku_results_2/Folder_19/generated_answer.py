def insert_before_character(s):
    result = []
    for char in s:
        if char == '5':
            result.append('h')
        result.append(char)
    return ''.join(result)