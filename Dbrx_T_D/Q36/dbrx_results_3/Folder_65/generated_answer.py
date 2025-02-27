def filter_chars(s: str) -> str:
    return ''.join((c for i, c in enumerate(s) if i < 58 or i >= 82 or (not 'F' < c < 'O') or (c not in s[58:82])))