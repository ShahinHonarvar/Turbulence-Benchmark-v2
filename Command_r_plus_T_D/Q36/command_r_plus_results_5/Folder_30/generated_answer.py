def filter_chars(s: str) -> str:
    filtered_chars = [c for c in s if not (23 < s.index(c) < 45 and '3' < c < 'I')]
    return ''.join(filtered_chars)