def filter_chars(s):
    filtered_chars = set((c for c in s[41:80] if 'f' <= c <= '|'))
    return ''.join((c for c in s if c not in filtered_chars))