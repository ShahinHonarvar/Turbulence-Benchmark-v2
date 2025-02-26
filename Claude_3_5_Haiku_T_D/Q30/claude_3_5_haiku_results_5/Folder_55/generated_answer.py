def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'u':
            result += 'U' + char
        else:
            result += char
    return result