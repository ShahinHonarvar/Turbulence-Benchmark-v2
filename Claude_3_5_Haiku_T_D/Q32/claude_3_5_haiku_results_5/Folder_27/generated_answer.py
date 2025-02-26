def insert_after_character(text):
    result = []
    for char in text:
        result.append(char)
        if char == 'N':
            result.append('j')
    return ''.join(result)