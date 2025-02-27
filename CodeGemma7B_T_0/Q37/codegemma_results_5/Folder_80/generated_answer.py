def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[36:80] or not (ch >= 'a' and ch <= 'i')])