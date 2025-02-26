def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'O':
            result += 'o' + char
        else:
            result += char
    return result