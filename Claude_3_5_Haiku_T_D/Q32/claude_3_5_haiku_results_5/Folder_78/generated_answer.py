def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'H':
            result += 'Hs'
        else:
            result += char
    return result