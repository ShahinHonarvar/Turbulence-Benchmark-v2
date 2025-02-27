def filter_chars(text):
    for i in range(476, 948):
        if text[i] > 'b' and text[i] < 'd':
            text = text[:i] + text[i + 1:]
    return text