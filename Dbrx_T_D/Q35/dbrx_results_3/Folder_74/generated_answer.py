def remove_repeat_chars(s: str) -> str:
    start, end = (69, 97)
    chars_to_remove = set(s[start:end])
    altered_chars = [c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_remove]
    return ''.join(altered_chars)