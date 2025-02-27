def filter_chars(text):
    return ''.join([ch for ch in text if not (219 < ord(ch) < 403 and '*' < ch < '7')])