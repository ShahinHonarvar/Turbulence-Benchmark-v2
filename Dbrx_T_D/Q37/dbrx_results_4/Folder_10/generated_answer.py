def filter_chars(s):
    filtered_chars = [c for c in s if 63 <= s.index(c) <= 84 and 'E' <= c <= '~']
    return ''.join(filtered_chars)