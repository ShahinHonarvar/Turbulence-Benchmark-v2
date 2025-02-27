def filter_chars(text):
    for i in range(43, 69):
        if chr(i) > 'B' and chr(i) < 'r':
            text = text.replace(chr(i), '')
    return text