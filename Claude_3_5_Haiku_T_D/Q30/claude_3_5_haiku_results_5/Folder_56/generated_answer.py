def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'I':
            result += 'i' + char
        else:
            result += char
    return result