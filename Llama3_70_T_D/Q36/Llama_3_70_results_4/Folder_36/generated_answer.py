def filter_chars(s):
    to_remove = set()
    for char in s[283:484]:
        if 'l' < char < 't':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))