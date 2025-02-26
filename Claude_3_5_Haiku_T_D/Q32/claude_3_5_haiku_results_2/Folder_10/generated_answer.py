def insert_after_character(text):
    result = []
    for char in text:
        result.append(char)
        if char == 'j':
            result.append('v')
    return ''.join(result)