def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'i':
            result.append('i')
    return ''.join(result)