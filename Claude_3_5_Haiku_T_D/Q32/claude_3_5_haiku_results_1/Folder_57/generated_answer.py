def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 's':
            result.append('w')
    return ''.join(result)