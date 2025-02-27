def filter_chars(text):
    for i in range(19, 23):
        if text[i] >= ']' and text[i] <= 't':
            text = text[:i] + text[i + 1:]
    return text