def filter_chars(s):
    filtered_chars = [c for c in s if c < 'A' or c > 'Q' or (c >= 'A' and c <= 'Q' and (c < s[38] or c > s[99]))]
    return ''.join(filtered_chars)