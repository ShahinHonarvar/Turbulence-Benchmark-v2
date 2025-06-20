def filter_chars(s):
    if len(s) <= 4:
        return s
    chars_to_remove = {s[i] for i in range(4, min(5, len(s) - 1)) if 'Y' < s[i] < 's'}
    return ''.join((c for c in s if c not in chars_to_remove))