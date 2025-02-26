def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'i':
            result += 'I' + char
        else:
            result += char
    return result