def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'j':
            result += 'v'
        result += char
    return result