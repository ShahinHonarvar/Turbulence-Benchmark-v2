def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'B':
            result += 'N' + char
        else:
            result += char
    return result