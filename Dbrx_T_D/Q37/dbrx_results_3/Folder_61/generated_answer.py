def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i not in range(5, 7) or c < 'G' or c > 'p'))