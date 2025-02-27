def filter_chars(text):
    for i in range(19, 33):
        if text[i] in 'f' <= text[i] <= 'o':
            text = text[:i] + text[i + 1:]
    return text