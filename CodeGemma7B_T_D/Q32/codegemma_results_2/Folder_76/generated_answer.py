def insert_after_character(s):
    result = []
    for char in s:
        if char == 'F':
            result.append(char)
            result.append('m')
        else:
            result.append(char)
    return ''.join(result)