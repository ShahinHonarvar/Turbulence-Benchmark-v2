def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'w':
            result += 'n'
    return result