def filter_chars(text):
    for i in range(33, 36):
        text = text.replace(chr(i), '')
    return text