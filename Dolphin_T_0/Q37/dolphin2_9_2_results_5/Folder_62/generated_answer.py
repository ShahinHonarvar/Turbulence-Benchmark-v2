def filter_chars(text):
    for i in range(10, 70):
        if text[i] >= 'I' and text[i] <= 'K':
            new_text = text[:i] + text[i + 1:]
    return new_text