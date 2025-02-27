def filter_chars(s):
    filtered_str = ''.join([c for c in s if not (50 <= ord(c) <= 92 and 'A' < c < 'Q')])
    return filtered_str