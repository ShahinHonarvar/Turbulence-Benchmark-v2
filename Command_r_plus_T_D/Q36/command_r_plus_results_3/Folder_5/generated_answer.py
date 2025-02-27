def filter_chars(s: str) -> str:
    filter_chars_set = set(s[55:66])
    filter_chars_set = {c for c in filter_chars_set if 'f' < c < '|'}
    s = ''.join((c for c in s if c not in filter_chars_set))
    return s