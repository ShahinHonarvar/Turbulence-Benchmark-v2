def insert_after_character(s):
    result = []
    for char in s:
        if char == '5':
            result.append(char)
            result.append('R')
        else:
            result.append(char)
    return ''.join(result)