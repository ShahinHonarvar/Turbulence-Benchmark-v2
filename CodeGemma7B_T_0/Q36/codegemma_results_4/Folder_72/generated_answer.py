def filter_chars(text):
    return ''.join([ch for ch in text if not (44 < ord(ch) < 68 and 'W' < ch < 'x')])