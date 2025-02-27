def filter_chars(s):
    to_remove = set()
    for i in range(73, 93):
        if i < len(s) and '<' < s[i] < 'J':
            to_remove.add(s[i])
    return ''.join([c for c in s if c not in to_remove])