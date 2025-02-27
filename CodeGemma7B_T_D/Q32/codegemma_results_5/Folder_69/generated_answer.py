def insert_after_character(text):
    result = ''
    for char in text:
        if char == ' ':
            result += char + 'P'
        else:
            result += char
    return result