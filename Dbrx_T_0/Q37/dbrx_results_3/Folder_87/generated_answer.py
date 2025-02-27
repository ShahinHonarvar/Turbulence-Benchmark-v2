def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('W'), ord('[') + 1))
    result = [c for i, c in enumerate(s) if i < 18 or i > 81 or ord(c) not in chars_to_remove]
    return ''.join(result)