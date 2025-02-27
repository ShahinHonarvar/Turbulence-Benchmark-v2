def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'P':
            result += char + 'V'
        else:
            result += char
    return result