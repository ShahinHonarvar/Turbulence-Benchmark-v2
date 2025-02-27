def insert_before_character(text):
    result = []
    for char in text:
        if char == ' ':
            result.extend(['X', char])
        else:
            result.append(char)
    return ''.join(result)