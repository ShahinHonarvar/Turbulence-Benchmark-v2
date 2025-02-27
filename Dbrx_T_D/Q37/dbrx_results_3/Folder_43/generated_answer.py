def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 15 <= s.index(c) <= 55 and 'W' <= c <= '{'][::-1]
    result = ''.join((c for c in s if c not in filtered_chars))
    return result