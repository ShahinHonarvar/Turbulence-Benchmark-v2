def filter_chars(text):
    for c in text[61:71]:
        if c >= '0' and c <= '@':
            text = text.replace(c, '')
    return text