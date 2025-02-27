def filter_chars(s: str) -> str:
    filter_set = set(s[44:48])
    filter_set = {c for c in filter_set if '+' < c < 'l'}
    return ''.join((c for c in s if c not in filter_set))