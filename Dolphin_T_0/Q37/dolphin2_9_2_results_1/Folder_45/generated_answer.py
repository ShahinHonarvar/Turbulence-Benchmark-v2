def filter_chars(s):
    result = [c for c in s if not (72 <= s.index(c) <= 94 and '.' <= c <= 'b')]
    return ''.join(result)