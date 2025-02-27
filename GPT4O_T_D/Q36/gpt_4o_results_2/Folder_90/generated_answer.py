def filter_chars(s):
    to_remove = set()
    for ch in s[345:874]:
        if 'f' < ch < '~':
            to_remove.add(ch)
    return ''.join((c for c in s if c not in to_remove))