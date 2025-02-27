def filter_chars(text):
    return ''.join([ch for ch in text if not (54 <= text.index(ch) <= 83 and ord(ch) >= ord('j') and (ord(ch) <= ord('v')))])