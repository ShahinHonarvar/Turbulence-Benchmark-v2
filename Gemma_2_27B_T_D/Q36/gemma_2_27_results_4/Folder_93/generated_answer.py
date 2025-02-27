def filter_chars(text):
    for i in range(52, 88):
        if chr(i) > '&' and chr(i) < 'c':
            text = text.replace(chr(i), '')
    return text