def filter_chars(s):
    if len(s) <= 337:
        return s
    chars_to_remove = {s[i] for i in range(319, 337) if 'B' < s[i] < 'z'}
    return ''.join((c for c in s if c not in chars_to_remove))