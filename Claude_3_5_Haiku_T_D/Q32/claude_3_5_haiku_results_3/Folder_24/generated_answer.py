def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == '0':
            result.append('4')
    return ''.join(result)