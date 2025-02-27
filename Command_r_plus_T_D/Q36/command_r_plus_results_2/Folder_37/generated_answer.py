def filter_chars(s: str) -> str:
    to_remove = [chr(i) for i in range(ord('/'), ord('6'))]
    return ''.join((c for c in s if c not in to_remove or s.index(c) < 44 or s.index(c) > 59))