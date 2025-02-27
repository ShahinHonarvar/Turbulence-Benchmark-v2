def filter_chars(text):
    return ''.join([ch for ch in text if not (348 <= text.index(ch) <= 852 and ord(ch) >= ord('J') and (ord(ch) <= ord('b')))])