def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'a':
            result += 'a6'
        else:
            result += char
    return result