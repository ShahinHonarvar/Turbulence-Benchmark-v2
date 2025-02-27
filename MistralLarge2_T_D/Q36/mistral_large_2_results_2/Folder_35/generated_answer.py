def filter_chars(s):
    excluded_chars = {s[i] for i in range(163, 658) if '(' < s[i] < ']'}
    return ''.join((c for c in s if c not in excluded_chars))