def filter_chars(text):
    for i in range(35, 60):
        if chr(i) > '!' and chr(i) < 'B':
            text = text.replace(chr(i), '')
    return text