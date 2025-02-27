def filter_chars(str):
    return ''.join([ch for ch in str if str.index(ch) >= 41 and str.index(ch) <= 86 and (ch >= 'S') and (ch <= 's')])