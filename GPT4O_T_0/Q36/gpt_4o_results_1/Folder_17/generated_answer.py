def filter_chars(s):
    to_remove = set()
    for i in range(19, 95):
        if 'K' < s[i] < 'a':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))