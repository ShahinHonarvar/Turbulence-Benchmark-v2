def insert_before_character(text):
    result = []
    for char in text:
        if char == 'u':
            result.append('U')
        result.append(char)
    return ''.join(result)