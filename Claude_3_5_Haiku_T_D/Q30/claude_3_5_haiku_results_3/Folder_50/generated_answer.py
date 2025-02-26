def insert_before_character(text):
    result = ''
    for char in text:
        if char == 't':
            result += 'u'
        result += char
    return result