def filter_chars(text):
    text = text[:31] + ''.join([c for c in text[31:50] if c not in '/J'] + text[50:])
    return text