def filter_chars(s):
    filtered = s[:172] + ''.join((c for c in s[172:636] if c <= 'c' or c >= 's')) + s[636:]
    return filtered