def insert_before_character(s):
    result = []
    for char in s:
        if char == 'r':
            result.append('w')
        result.append(char)
    return ''.join(result)