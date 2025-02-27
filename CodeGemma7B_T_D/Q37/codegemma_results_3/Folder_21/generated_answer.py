def filter_chars(text):
    return ''.join([ch for ch in list(text) if 603 <= ord(ch) <= 759 and ord(ch) >= ord('Q') <= ord('h')])