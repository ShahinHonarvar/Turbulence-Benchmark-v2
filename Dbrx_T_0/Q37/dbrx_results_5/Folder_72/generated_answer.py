def filter_chars(s):
    filtered_chars = [c for c in s if 35 <= s.index(c) <= 51 and 'H' <= c <= 's']
    return ''.join(filtered_chars)