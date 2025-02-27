def filter_chars(s):
    to_remove = {c for c in s[1:8] if 'L' <= c <= 'a'}
    return ''.join((c for c in s if c not in to_remove))