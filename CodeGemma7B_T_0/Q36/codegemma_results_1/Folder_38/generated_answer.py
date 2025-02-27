def filter_chars(text):
    for i in range(44, 48):
        if text[i] > '+' and text[i] < 'l':
            text = text[:i] + text[i + 1:]
    return text