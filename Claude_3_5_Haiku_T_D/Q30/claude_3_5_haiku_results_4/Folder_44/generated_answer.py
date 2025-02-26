def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'g':
            result += 'M'
        result += char
    return result