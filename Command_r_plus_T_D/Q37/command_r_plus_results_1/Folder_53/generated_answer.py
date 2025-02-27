def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if not (83 <= i <= 99 and '*' <= c <= 'j')]
    return ''.join(filtered_chars)