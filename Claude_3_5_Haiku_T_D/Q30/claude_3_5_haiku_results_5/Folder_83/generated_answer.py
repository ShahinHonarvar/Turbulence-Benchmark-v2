def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'E':
            result += 'e' + char
        else:
            result += char
    return result