def filter_chars(s):
    modified = [c for c in s if 25 <= s.index(c) <= 97 and c >= 'm' and (c <= 'w')]
    return ''.join(modified)