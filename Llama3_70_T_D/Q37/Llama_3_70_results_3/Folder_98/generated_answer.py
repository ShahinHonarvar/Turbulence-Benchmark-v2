def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(8, 10) if 'R' <= s[i] <= 't'])
    return ''.join([c for c in s if c not in chars_to_remove])