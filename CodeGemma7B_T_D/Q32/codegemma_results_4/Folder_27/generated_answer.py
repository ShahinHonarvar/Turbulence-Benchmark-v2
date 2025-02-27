def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'N':
            result += char + 'j'
        else:
            result += char
    return result