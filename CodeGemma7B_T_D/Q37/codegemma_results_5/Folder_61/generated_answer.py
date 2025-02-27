def filter_chars(s):
    return ''.join([ch for ch in s if not (5 <= idx <= 6 and 'G' <= ch <= 'p') or idx < 5 or idx > 6])