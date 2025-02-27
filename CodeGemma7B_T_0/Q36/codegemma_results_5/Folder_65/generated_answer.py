def filter_chars(text):
    for i in range(58, 82):
        if text[i] > 'F' and text[i] < 'O':
            text = text[:i] + text[i + 1:]
    return text