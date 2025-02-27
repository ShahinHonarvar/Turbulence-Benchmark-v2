def filter_chars(text):
    for i in range(770, 971):
        if text[i] in '-D':
            text = text[:i] + text[i + 1:]
    return text