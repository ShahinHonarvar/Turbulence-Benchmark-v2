def filter_chars(s):
    to_remove = set()
    for i in range(49, 75):
        if '6' < s[i] < '_':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))