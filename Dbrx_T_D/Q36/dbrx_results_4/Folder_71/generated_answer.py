def filter_chars(s: str) -> str:
    start_idx = 82
    end_idx = 89
    chars_to_remove = set(range(ord('*') + 1, ord('[')))
    for i in range(start_idx, end_idx):
        if ord(s[i]) in chars_to_remove:
            s = s[:i] + s[i + 1:]
    return s