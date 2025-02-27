def insert_before_character(text):
    result = []
    for char in text:
        if char == 'm':
            result.append('N')
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)