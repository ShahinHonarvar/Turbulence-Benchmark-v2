def filter_chars(s):
    filtered_chars = [c for c in s if not (32 <= ord(c) <= 46 and '0' <= c <= 'k')]
    return ''.join(filtered_chars)