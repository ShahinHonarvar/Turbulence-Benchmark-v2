def insert_after_character(str):
    result = []
    for char in str:
        if char == 'A':
            result.append(char)
            result.append('a')
        else:
            result.append(char)
    return ''.join(result)