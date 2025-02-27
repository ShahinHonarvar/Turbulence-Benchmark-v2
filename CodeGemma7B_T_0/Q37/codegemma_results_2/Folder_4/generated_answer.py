def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[19:34] or not (ch >= 'S' and ch <= '{')])