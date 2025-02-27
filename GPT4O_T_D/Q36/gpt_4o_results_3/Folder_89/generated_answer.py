def filter_chars(s):
    if len(s) <= 57:
        return s
    target_chars = set()
    for i in range(58, min(69, len(s))):
        if '(' < s[i] < 'W':
            target_chars.add(s[i])
    return ''.join((c for c in s if c not in target_chars))