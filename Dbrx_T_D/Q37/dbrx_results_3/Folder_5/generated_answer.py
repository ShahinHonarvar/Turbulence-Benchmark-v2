def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if 24 <= s.index(c) <= 82 and '5' <= c <= '<']
    return ''.join([c for c in s if c not in set(filtered_chars)])