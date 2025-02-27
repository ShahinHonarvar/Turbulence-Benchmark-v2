def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(ord('F') + 1, ord('O'))]
    return ''.join([c for c in s if c not in filter_range])