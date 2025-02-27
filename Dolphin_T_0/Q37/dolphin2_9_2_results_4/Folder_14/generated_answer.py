def filter_chars(s):
    ob = [c for c in s if c not in s[35:99] and 'A' <= c <= 'b']
    s = [c for c in s if c not in ob]
    return ''.join(s)