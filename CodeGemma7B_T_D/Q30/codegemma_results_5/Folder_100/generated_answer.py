def insert_before_character(text):
    result = ''
    for char in text:
        if char == '0':
            result += ' ' + char
        else:
            result += char
    return result