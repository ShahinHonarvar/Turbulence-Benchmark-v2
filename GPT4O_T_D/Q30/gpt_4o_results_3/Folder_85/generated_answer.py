def insert_before_character(s):
    result = []
    for char in s:
        if char == 'o':
            result.append('a')
        result.append(char)
    return ''.join(result)