def filter_chars(s: str) -> str:
    filter_range = range(10, 16)
    filter_chars_set = set((chr(i) for i in range(ord('t') + 1, ord('v'))))
    filtered_s = ''.join([c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars_set])
    return filtered_s