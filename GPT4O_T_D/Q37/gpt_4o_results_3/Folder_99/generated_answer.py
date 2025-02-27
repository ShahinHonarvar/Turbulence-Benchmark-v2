def filter_chars(s):
    to_remove = set()
    for i in range(373, min(902, len(s))):
        if 'T' <= s[i] <= 'h':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))