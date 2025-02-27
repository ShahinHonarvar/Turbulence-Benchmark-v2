def insert_after_character(text):
    result = []
    for char in text:
        result.append(char)
        if char == 'U':
            result.append('U')
    return ''.join(result)