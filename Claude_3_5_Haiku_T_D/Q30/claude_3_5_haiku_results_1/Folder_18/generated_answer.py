def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'K':
            result += 'l' + char
        else:
            result += char
    return result