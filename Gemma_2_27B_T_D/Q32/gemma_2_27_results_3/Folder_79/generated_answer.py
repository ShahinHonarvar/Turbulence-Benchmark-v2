def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'E':
            result += 'E'
    return result