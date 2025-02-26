def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'o':
            result += 'O' + char
        else:
            result += char
    return result