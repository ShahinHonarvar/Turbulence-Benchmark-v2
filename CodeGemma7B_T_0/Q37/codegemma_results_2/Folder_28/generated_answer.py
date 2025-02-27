def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[20:80] or not (ch >= '!' and ch <= 'T')])