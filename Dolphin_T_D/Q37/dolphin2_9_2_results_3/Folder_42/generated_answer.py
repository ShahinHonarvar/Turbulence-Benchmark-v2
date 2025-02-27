def filter_chars(s):
    c = set([c for i, c in enumerate(s, start=1) if 73 <= i <= 74 and 'U' <= c <= 'l'])
    return ''.join((ch for ch in s if ch not in c))