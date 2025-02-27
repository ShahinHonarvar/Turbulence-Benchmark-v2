def filter_chars(s):
    remove_chars = {s[i] for i in range(27, 86) if '!' <= s[i] <= 'B'}
    return ''.join((c for c in s if c not in remove_chars))