def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'e':
            result += 'ee'
        else:
            result += char
    return result