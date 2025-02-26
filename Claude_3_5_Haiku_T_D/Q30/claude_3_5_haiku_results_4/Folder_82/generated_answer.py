def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'I':
            result += 'I'
        result += char
    return result