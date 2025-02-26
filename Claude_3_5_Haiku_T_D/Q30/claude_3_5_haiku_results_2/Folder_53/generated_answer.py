def insert_before_character(text):
    result = []
    for char in text:
        if char == 'i':
            result.append('I')
        result.append(char)
    return ''.join(result)