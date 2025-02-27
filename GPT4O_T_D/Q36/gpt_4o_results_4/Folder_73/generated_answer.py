def filter_chars(s: str) -> str:
    to_remove = {c for c in s[67:90] if '#' < c < 'T'}
    return ''.join((c for c in s if c not in to_remove))