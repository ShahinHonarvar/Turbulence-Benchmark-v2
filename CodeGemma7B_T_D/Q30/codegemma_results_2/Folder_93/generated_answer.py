def insert_before_character(text):
    result = []
    for char in text:
        if char == 'Y':
            result.append('4')
        result.append(char)
    return ''.join(result)