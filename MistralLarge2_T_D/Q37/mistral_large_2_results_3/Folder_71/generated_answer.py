def filter_chars(s):
    to_remove = set()
    for i in range(32, 47):
        if '0' <= s[i] <= 'k':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))