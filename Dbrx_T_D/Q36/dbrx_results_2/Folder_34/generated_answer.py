def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c not in filter(lambda x: '?' < x < 'm', s[10:79])))