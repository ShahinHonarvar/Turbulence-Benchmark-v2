def filter_chars(s):
    to_remove = set()
    for i in range(19, min(len(s), 93)):
        if '8' <= s[i] <= 'm':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))