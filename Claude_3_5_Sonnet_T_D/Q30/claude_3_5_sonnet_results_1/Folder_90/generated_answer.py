def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'U':
            result += 'F'
        result += char
    return result