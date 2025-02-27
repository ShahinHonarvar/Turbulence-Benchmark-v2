def filter_chars(text):
    return ''.join([ch for ch in text if not (56 < ord(ch) < 86 and '+' < ch < 'w')])