def filter_chars(text):
    return ''.join([ch for ch in text if not (text.index(ch) in range(24, 83) and ch >= '5' and (ch <= '<'))])