def filter_chars(s):
    return ''.join((c for c in s if not 42 <= s.index(c) <= 97 or not '*' <= c <= 'b'))