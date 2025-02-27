def filter_chars(s):
    to_remove = set()
    for i in range(min(len(s), 27), min(len(s), 86)):
        if 'c' <= s[i] <= 'i':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))