def filter_chars(s):
    if len(s) <= 21:
        return s
    to_filter = set()
    for i in range(21, min(44, len(s))):
        if '+' <= s[i] <= '8':
            to_filter.add(s[i])
    return ''.join((c for c in s if c not in to_filter))