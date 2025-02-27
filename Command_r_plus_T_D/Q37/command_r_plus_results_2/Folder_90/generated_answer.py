def filter_chars(s: str) -> str:
    filter_range = range(348, 853)
    filter_chars_set = set((chr(i) for i in range(ord('J'), ord('b') + 1)))
    filtered_string = ''.join((c for i, c in enumerate(s) if i not in filter_range or c not in filter_chars_set))
    return filtered_string