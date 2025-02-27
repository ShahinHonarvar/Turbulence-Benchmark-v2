def filter_chars(s):
    to_remove = s[82:86]
    filtered = [c for c in s if c not in to_remove or c <= '!' or c >= 's']
    return ''.join(filtered)