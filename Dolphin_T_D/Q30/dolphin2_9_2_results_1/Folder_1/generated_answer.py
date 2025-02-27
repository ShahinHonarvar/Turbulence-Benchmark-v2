def insert_before_character(text):
    result = ''
    for i in range(len(text)):
        if text[i] == 'U':
            result += 'T'
        result += text[i]
    return result