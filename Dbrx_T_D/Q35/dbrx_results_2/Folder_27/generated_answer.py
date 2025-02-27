def remove_repeat_chars(s: str) -> str:
    start, end = (86, 89)
    chars_to_remove = set(s[start:end])
    new_s = [c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_remove]
    return ''.join(new_s)