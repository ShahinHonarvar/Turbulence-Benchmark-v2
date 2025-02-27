def filter_chars(text):
    for i in range(32, 61):
        if chr(i) > '3' and chr(i) < 'D':
            text = text.replace(chr(i), '')
    return text