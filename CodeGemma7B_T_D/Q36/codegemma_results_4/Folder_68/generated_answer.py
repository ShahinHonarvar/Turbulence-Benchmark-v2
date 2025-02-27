def filter_chars(s):
    return ''.join([ch for ch in s if not (ch > '8' and ch < 'm' and (1 < ord(ch) < 9))])