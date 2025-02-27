def filter_chars(text):
    for i in range(39, 87):
        if chr(i) > '!' and chr(i) < '}':
            text = text.replace(chr(i), '')
    return text