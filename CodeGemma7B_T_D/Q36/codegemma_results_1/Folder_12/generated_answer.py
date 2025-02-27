def filter_chars(s):
    return ''.join([ch for ch in s if ch > 'm' and ch < 'w' and (ch not in s[32:84])])