def insert_before_character(text):
    result = []
    for char in text:
        if char == 'c':
            result.append('G')
            result.append(char)
        else:
            result.append(char)
    return ''.join(result)