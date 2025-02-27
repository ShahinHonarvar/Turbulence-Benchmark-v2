def filter_chars(s):
    forbidden_chars = {s[i] for i in range(1, 8) if 'L' <= s[i] <= 'a'}
    return ''.join((c for c in s if c not in forbidden_chars))