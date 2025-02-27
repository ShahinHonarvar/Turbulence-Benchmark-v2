def filter_chars(s):
    filtered_chars = [c for c in s if not (603 <= s.index(c) <= 759 and 'Q' <= c <= 'h')]
    return ''.join(filtered_chars)