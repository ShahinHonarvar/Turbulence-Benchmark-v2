def filter_chars(s):
    chars_to_remove = {s[i] for i in range(83, 100) if '*' <= s[i] <= 'j'}
    return ''.join((c for c in s if c not in chars_to_remove))