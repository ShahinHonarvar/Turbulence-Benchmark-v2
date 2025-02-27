def filter_chars(text):
    return ''.join([ch for ch in text if not (32 < ord(ch) < 84 and 'm' < ch < 'w')])