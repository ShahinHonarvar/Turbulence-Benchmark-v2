def insert_after_character(text):
    result = ''
    for i in range(len(text)):
        result += text[i]
        if text[i] == 'F':
            result += 'o'
    return result