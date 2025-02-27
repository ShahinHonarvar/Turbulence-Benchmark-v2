def filter_chars(s):
    to_remove = set()
    for i in range(45, 68):
        if 'W' < s[i] < 'x':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))