def filter_chars(s: str) -> str:
    start_index = 343
    end_index = 665
    chars_to_remove = set(range(ord('%') + 1, ord('U')))
    return ''.join((c for i, c in enumerate(s) if i < start_index or i >= end_index or c not in chars_to_remove))