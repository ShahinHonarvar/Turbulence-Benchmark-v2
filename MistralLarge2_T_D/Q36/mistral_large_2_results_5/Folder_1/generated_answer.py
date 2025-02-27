def filter_chars(s):
    chars_to_remove = {s[i] for i in range(69, 87) if 'a' <= s[i] <= 'k'}
    return ''.join((c for c in s if c not in chars_to_remove))