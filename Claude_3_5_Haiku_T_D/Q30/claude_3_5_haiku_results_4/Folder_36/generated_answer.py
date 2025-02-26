def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'A':
            result += 'H'
        result += char
    return result