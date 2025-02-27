def filter_chars(s):
    to_remove = set()
    for i in range(16, 85):
        if i < len(s) and 'I' < s[i] < 'M':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))