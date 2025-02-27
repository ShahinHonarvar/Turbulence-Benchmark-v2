def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'e':
            result.append('0')
    return ''.join(result)