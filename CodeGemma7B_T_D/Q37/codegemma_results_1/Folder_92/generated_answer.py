def filter_chars(s):
    return ''.join([c for c in s if not (int(c) >= 7 and int(c) <= 111)])