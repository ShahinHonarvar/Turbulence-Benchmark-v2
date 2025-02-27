def filter_chars(s):
    to_remove = set()
    for i in range(70, 97):
        if 'V' < s[i] < 'j':
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))