def insert_before_character(s):
    result = []
    for char in s:
        if char == 'Q':
            result.append('I')
        result.append(char)
    return ''.join(result)