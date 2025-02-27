def insert_before_character(text):
    result = []
    for char in text:
        if char == 'N':
            result.append('z')
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)