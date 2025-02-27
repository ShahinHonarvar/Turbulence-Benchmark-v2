def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('+'), ord('8') + 1))
    chars_to_keep = [c for i, c in enumerate(s) if i < 21 or i > 43 or c not in chars_to_remove]
    return ''.join(chars_to_keep)