def filter_chars(text):
    for i in range(90, 97):
        text = text.replace(chr(i), '')
    return text