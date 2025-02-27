def filter_chars(text):
    return ''.join([ch for ch in text if ch not in range(45, 60) or (ch > '/' and ch < '6')])