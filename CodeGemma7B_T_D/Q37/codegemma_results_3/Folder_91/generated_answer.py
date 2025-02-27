def filter_chars(text):
    for i in range(7, 9):
        while i < len(text) and text[i] >= 'B' and (text[i] <= 'H'):
            text = text[:i] + text[i + 1:]
    return text