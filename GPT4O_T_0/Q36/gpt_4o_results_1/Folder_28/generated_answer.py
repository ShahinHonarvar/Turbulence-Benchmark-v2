def filter_chars(s):
    to_remove = set()
    for i in range(32, 73):
        if 'M' < s[i] < 'j':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))