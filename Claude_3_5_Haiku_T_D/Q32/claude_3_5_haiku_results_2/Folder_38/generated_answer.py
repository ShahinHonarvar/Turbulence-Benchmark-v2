def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'X':
            result.append('6')
    return ''.join(result)