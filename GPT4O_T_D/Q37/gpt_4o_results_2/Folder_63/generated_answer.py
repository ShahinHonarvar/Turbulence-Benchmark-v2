def filter_chars(s):
    if len(s) < 43:
        return s
    chars_to_remove = {s[i] for i in range(42, min(93, len(s))) if '/' <= s[i] <= 'a'}
    return ''.join((c for c in s if c not in chars_to_remove))