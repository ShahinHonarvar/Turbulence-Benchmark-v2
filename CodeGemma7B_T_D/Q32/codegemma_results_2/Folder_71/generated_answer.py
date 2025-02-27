def insert_after_character(text):
    result = ''
    for character in text:
        if character == '2':
            result += '2S'
        else:
            result += character
    return result