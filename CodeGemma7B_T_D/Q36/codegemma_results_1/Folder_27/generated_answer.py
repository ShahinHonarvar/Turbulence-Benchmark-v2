def filter_chars(text):
    return ''.join([ch for i, ch in enumerate(text) if i not in range(48, 75) or not (ch > '6' and ch < '_')])