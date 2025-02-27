def filter_chars(s):
    to_remove = set()
    for i in range(72, 95):
        if i < len(s) and '.' <= s[i] <= 'b':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))