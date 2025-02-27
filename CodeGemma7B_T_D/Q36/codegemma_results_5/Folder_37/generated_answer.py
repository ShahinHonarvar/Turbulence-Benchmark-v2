def filter_chars(s):
    return ''.join([ch for ch in s if not (44 < ord(ch) < 59 and ch > '/' and (ch < '6'))])