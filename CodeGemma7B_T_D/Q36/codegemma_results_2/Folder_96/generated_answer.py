def filter_chars(text):
    for i in range(38, 81):
        text = text.replace(chr(i), '')
    return text