def filter_chars(text):
    for i in range(24, 80):
        if text[i] >= 'a' and text[i] <= 'f':
            text = text[:i] + text[i + 1:]
    return text