def filter_chars(s):
    chars_to_remove = {s[i] for i in range(227, 236) if 'D' <= s[i] <= 'u'}
    return ''.join((c for c in s if c not in chars_to_remove))