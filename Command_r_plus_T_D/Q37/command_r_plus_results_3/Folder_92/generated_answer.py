def filter_chars(s: str) -> str:
    filter_range = range(4, 5)
    filter_chars_set = set((chr(i) for i in range(ord('7'), ord('o') + 1)))
    return ''.join((c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars_set))