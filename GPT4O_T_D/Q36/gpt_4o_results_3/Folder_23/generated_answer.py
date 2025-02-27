def filter_chars(s):
    if len(s) <= 21:
        return s
    start = 21
    end = min(25, len(s) - 1)
    to_remove = set((c for c in s[start + 1:end] if '5' < c < '}'))
    return ''.join((c for c in s if c not in to_remove))