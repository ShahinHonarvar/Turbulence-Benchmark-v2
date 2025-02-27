def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'j':
            result += char + 'q'
        else:
            result += char
    return result