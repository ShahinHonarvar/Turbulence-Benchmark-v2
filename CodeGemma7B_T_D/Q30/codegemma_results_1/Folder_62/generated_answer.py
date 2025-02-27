def insert_before_character(x):
    result = []
    for char in x:
        if char == ' ':
            result.append('o')
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)