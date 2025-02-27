def filter_chars(text):
    for i in range(3, 9):
        if text[i] > '*' and text[i] < 'E':
            text = text[:i] + text[i + 1:]
    return text