def filter_chars(text):
    for c in text:
        if 15 <= text.index(c) <= 55 and 'W' <= c <= '{':
            text = text.replace(c, '')
    return text