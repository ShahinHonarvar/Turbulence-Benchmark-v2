def filter_chars(s):
    indices = set(range(32, 47))
    to_remove = {s[i] for i in range(len(s)) if i in indices and '0' <= s[i] <= 'k'}
    return ''.join((c for c in s if c not in to_remove))