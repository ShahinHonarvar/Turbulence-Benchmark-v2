def insert_before_character(s):
    result = []
    for char in s:
        if char == 'Y':
            result.append('4')
        result.append(char)
    return ''.join(result)