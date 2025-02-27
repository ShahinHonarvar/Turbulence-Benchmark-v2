def filter_chars(s):
    if len(s) < 93:
        return s
    else:
        remove_chars = {s[i] for i in range(86, 93) if '!' <= s[i] <= 's'}
        return ''.join((c for c in s if c not in remove_chars))