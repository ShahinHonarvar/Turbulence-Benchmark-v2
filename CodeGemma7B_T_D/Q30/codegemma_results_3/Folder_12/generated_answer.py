def insert_before_character(text):
    result = ''
    i = 0
    while i < len(text):
        if text[i] == 'I':
            result += text[i - 1] + ' '
        result += text[i]
        i += 1
    return result