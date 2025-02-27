def filter_chars(text):
    for i in range(20, 63):
        for c in text:
            if c == text[i]:
                text = text.replace(c, '')
    return text