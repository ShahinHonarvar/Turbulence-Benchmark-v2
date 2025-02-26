def insert_after_character(text):
    result = []
    for char in text:
        result.append(char)
        if char == 'O':
            result.append('o')
    return ''.join(result)