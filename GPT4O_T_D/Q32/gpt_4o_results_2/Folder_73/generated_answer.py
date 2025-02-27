def insert_after_character(s):
    result = []
    for char in s:
        result.append(char)
        if char == 'R':
            result.append('V')
    return ''.join(result)