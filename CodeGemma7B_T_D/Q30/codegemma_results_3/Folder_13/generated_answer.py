def insert_before_character(text):
    result = []
    for char in text:
        if char == 'x':
            result.append('N')
        result.append(char)
    return ''.join(result)