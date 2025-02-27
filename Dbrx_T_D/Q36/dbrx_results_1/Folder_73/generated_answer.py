def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c < '#' or (c > 'T' and c < 'Z') or (c > 'Z' and c not in range(ord('G'), ord('T')))))