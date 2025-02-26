def insert_after_character(text):
    result = []
    for char in text:
        result.append(char)
        if char == '2':
            result.append('S')
    return ''.join(result)