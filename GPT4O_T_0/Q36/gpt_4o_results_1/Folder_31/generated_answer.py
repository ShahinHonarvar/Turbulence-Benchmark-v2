def filter_chars(s):
    to_remove = set()
    for i in range(15, 75):
        if i < len(s) and '9' < s[i] < 'K':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))