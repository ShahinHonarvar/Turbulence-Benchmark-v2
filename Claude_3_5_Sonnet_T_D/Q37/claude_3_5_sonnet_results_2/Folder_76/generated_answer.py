def filter_chars(s):
    to_remove = set()
    for i in range(379, 899):
        if i < len(s) and 'M' <= s[i] <= 'v':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))