def filter_chars(text):
    return ''.join([ch for ch in text if not (50 < ord(ch) < 92 and 'A' < ch < 'Q')])