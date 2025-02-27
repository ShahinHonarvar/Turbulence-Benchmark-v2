def filter_chars(s):
    return ''.join([ch for ch in s if not (ch >= 'c' and ch <= 'i' and (27 <= ord(ch) <= 85))])