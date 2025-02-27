def insert_after_character(text):
    result = ''
    i = 0
    while i < len(text):
        if text[i] == 'U':
            result += text[i] + 'F'
        else:
            result += text[i]
        i += 1
    return result