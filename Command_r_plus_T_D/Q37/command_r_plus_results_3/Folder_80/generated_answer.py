def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('a'), ord('i') + 1)))
    filtered_string = ''.join((c for i, c in enumerate(s) if 36 <= i <= 79 and c not in chars_to_remove))
    return filtered_string