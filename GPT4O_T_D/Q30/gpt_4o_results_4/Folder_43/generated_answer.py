def insert_before_character(s):
    result = []
    for char in s:
        if char == 't':
            result.append('G')
        result.append(char)
    return ''.join(result)