def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'O':
            result += 'd'
        result += char
    return result