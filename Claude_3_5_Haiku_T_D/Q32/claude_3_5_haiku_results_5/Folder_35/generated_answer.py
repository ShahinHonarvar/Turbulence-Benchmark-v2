def insert_after_character(text):
    result = ''
    for char in text:
        result += char
        if char == '9':
            result += 'M'
    return result