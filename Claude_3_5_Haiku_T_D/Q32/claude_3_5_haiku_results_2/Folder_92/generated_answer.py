def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'a':
            result.append('a')
    return ''.join(result)