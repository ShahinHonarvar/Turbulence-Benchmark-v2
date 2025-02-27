def filter_chars(s):
    to_remove = set()
    for i in range(10, 53):
        if 'A' <= s[i] <= 'T':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))