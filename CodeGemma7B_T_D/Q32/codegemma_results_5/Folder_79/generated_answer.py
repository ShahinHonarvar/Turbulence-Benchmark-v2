def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'E':
            result += char + 'E'
        else:
            result += char
    return result