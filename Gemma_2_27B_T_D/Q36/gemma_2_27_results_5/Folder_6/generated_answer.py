def filter_chars(text):
    for i in range(31, 70):
        if chr(i) > 'B' and chr(i) < 'v':
            text = text.replace(chr(i), '')
    return text