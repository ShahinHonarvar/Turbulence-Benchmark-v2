def filter_chars(text):
    return ''.join([ch for ch in text if not (ch >= 'i' and ch <= 'v' and (11 <= text.index(ch) <= 72))])