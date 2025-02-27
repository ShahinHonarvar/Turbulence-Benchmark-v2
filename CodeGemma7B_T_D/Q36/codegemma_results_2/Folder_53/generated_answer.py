def filter_chars(text):
    for c in range(90, 97):
        text = text.replace(chr(c), '')
    return text