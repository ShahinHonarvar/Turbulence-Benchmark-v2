def filter_chars(s):
    if len(s) <= 324:
        return s
    to_remove = {c for c in set(s[324:526]) if ')' < c < 'O'}
    return ''.join((c for c in s if c not in to_remove or not 324 < s.index(c) < 526))