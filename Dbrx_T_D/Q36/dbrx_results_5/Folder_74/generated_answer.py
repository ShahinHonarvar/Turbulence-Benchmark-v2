def filter_chars(s: str) -> str:
    return ''.join((c for c in s if c not in range(ord('>') + 1, ord('A')) or c not in range(ord('B'), ord('[') + 1)))