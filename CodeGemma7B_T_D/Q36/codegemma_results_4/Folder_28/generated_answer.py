def filter_chars(text):
    text = ''.join((c for c in text if ord(c) not in range(32, 72)))
    return text