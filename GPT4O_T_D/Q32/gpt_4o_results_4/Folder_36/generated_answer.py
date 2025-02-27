def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'A':
            result.append('H')
    return ''.join(result)