def filter_chars(text):
    for i in range(2, 4):
        if text[i] >= '5' and text[i] <= '_':
            text = text[:i] + text[i + 1:]
    return text