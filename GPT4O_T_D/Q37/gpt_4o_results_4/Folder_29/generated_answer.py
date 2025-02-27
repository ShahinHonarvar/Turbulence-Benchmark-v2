def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('&'), ord('v') + 1)))
    removal_candidates = set(s[12:89]).intersection(chars_to_remove)
    return ''.join((c for c in s if c not in removal_candidates))