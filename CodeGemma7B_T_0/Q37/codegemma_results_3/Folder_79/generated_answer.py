def filter_chars(text):
    return ''.join([ch for ch in text if not (ch >= '@' and ch <= 'T' and (10 <= text.index(ch) <= 52))])