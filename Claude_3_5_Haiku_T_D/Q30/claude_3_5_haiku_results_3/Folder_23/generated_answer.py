def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'b':
            result += 'y'
        result += char
    return result