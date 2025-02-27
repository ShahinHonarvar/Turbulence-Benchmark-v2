def remove_repeat_chars(s: str) -> str:
    start, end = (57, 84)
    chars_to_remove = set(s[start - 1:end - 1])
    return ''.join((c for i, c in enumerate(s) if i not in range(start - 1, end - 1) or c not in chars_to_remove))