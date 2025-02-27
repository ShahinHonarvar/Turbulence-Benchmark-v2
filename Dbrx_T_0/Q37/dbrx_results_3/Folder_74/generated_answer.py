def filter_chars(s):
    filtered_chars = [c for c in s if 19 <= s.index(c) <= 32 and 'f' <= c <= 'o']
    return ''.join(filtered_chars)