def filter_chars(s):
    filtered_chars = [c for c in s if 18 <= s.index(c) <= 81 and 'W' <= c <= '[']
    return ''.join(filtered_chars)