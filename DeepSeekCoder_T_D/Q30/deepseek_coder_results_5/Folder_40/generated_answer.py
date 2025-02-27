def insert_before_character(s):
    result = []
    for char in s:
        if char == 'e':
            result.append('e')
        result.append(char)
    return ''.join(result)