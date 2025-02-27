def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if 58 <= i < 81 and c <= '5' or c >= '>' or i < 58 or (i >= 81)))