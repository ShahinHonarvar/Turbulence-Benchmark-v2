def filter_chars(s):
    return ''.join([c for c in s if not (c >= '>' and c <= '_' and (521 <= s.index(c) <= 722))])