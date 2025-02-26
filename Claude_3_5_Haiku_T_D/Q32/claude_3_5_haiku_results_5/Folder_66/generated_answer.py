def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'k':
            result += 'k'
    return result