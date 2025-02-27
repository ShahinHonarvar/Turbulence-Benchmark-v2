def filter_chars(text):
    for i in range(323, 526):
        if text[i] > ')' and text[i] < 'O':
            text = text[:i] + text[i + 1:]
    return text