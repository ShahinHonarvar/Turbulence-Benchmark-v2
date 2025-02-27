def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'j':
            result += 'q' + char
        else:
            result += char
    return result