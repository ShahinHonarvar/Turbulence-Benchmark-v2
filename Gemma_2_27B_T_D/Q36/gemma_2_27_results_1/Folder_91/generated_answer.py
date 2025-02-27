def filter_chars(text):
    for i in range(4):
        if text[i] > '$' and text[i] < '?':
            text = text.replace(text[i], '')
    return text