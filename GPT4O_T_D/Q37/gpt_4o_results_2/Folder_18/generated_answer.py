def filter_chars(s):
    to_remove = set()
    for i in range(770, min(971, len(s))):
        if '-' <= s[i] <= 'D':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))