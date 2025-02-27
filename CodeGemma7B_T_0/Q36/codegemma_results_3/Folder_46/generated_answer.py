def filter_chars(text):
    for i in range(19, 69):
        if text[i] > '<' and text[i] < 'C':
            text = text[:i] + text[i + 1:]
    return text