def filter_chars(s):
    if len(s) <= 45:
        return s
    to_remove = set()
    for c in s[45:59]:
        if '/' < c < '6':
            to_remove.add(c)
    return ''.join(filter(lambda x: x not in to_remove, s))