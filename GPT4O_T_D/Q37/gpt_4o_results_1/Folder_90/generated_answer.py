def filter_chars(s):
    to_remove = set()
    for i in range(348, min(853, len(s))):
        if 'J' <= s[i] <= 'b':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))