def filter_chars(text):
    for i in range(36, 41):
        for c in text:
            if c == text[i]:
                text = text.replace(c, '')
    return text