def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'F':
            result += 'm'
    return result