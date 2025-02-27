def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not 35 <= s.index(c) <= 40 or c < ')' or c > 'l']
    return ''.join(filtered_chars)