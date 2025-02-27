def filter_chars(s):
    to_remove = set()
    for i in range(51, 78):
        if 'V' <= s[i] <= 'Y':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))