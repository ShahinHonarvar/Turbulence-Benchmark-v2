def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'T':
            result += 'V' + char
        else:
            result += char
    return result