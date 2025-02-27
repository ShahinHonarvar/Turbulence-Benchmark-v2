def filter_chars(s):
    if len(s) < 74:
        return s
    to_remove = set()
    for char in s[71:74]:
        if 'A' < char < 'U':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))