def filter_chars(text):
    for i in range(50, 92):
        if chr(i) > 'A' and chr(i) < 'Q':
            text = text.replace(chr(i), '')
    return text