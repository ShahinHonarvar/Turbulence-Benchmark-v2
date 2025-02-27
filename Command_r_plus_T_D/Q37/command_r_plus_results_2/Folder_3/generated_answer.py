def filter_chars(s: str) -> str:
    filter_range = range(37, 57)
    filter_chars_set = set((chr(i) for i in range(ord('6'), ord('_') + 1)))
    filtered_s = ''.join((c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars_set))
    return filtered_s