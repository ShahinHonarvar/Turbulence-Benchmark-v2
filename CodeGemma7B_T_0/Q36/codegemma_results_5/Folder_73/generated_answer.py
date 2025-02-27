def filter_chars(text):
    return ''.join([ch for ch in text if ch not in range(66, 91) or (ch > '#' and ch < 'T')])