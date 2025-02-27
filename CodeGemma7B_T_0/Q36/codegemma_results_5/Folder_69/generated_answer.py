def filter_chars(text):
    return ''.join([ch for ch in text if not (343 < ord(ch) < 665 and '%' < ch < 'U')])