def filter_chars(text):
    for i in range(42, 67):
        if chr(i) > '6' and chr(i) < 'g':
            text = text.replace(chr(i), '')
    return text