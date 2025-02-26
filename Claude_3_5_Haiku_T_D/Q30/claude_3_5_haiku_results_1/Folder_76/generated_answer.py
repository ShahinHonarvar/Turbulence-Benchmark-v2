def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'F':
            result += 'm'
        result += char
    return result