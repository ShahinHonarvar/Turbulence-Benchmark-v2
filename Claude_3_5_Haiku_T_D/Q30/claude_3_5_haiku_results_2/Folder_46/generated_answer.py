def insert_before_character(text):
    result = []
    for char in text:
        if char == '6':
            result.append('W')
        result.append(char)
    return ''.join(result)