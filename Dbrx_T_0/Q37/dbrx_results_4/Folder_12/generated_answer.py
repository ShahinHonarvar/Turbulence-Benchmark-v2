def filter_chars(s):
    filtered_chars = [c for c in s if 19 <= s.index(c) <= 90 and 'F' <= c <= 'h']
    return ''.join(filtered_chars)