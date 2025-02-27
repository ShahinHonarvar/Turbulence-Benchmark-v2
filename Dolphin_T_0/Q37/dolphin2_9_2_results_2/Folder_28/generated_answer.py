def filter_chars(s):
    return ''.join([c for c in s if (20 <= s.index(c) <= 79 and '!' <= c <= 'T') and s.count(c) == 1])