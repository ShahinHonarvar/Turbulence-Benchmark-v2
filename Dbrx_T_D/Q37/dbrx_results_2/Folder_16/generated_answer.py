def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 225 <= s.index(c) <= 381 and 'D' <= c <= 'Y']
    return ''.join((c for c in s if c not in filtered_chars))