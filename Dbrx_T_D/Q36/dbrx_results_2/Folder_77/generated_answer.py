def filter_chars(s):
    filtered_chars = [c for c in s[220:419] if '-' > c or c > 'v' or s[220:419].index(c) < s[220:419].index(c) if c > '-' and c < 'v']
    return s[:220] + ''.join(filtered_chars) + s[419:]