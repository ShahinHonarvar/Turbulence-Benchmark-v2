def filter_chars(s):
    return ''.join([ch for i, ch in enumerate(s) if not (503 <= i <= 753 and ch >= '9' and (ch <= 'w'))])