def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'a':
            result += '6' + char
        else:
            result += char
    return result