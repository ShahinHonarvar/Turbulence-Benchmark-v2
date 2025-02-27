def filter_chars(s):
    to_remove = set()
    for i in range(171, 636):
        if 'c' < s[i] < 's':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))