def filter_chars(s):
    to_remove = set()
    for i in range(22, 86):
        if '7' <= s[i] <= 'e':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))