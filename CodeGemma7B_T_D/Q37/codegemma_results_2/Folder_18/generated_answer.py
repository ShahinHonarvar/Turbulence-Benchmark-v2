def filter_chars(s):
    return ''.join([c for c in s[:770] + s[970:] if c not in s[770:970]])