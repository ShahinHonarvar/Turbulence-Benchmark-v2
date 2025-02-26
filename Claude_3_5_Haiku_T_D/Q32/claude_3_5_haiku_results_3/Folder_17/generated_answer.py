def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'Q':
            result += 'I'
    return result