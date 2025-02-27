def filter_chars(s):
    to_remove = set()
    for i in range(11, min(33, len(s))):
        if '!' <= s[i] <= '@':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))