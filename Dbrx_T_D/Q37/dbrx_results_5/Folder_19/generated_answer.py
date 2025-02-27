def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('E'), ord('t') + 1)) & set(range(35, 89 + 1))
    return ''.join((c for i, c in enumerate(s) if i not in chars_to_remove))