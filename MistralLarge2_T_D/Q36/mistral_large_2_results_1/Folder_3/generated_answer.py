def filter_chars(s):
    to_remove = {s[i] for i in range(42, 78) if '!' < s[i] < '?'}
    return ''.join((c for c in s if c not in to_remove))