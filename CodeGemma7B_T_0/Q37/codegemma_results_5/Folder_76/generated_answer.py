def filter_chars(text):
    return ''.join([ch for ch in text if not (text.index(ch) in range(379, 899) and ch >= 'M' and (ch <= 'v'))])