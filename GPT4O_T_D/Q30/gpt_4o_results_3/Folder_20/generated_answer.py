def insert_before_character(s):
    result = []
    for char in s:
        if char == 'C':
            result.append('H')
        result.append(char)
    return ''.join(result)