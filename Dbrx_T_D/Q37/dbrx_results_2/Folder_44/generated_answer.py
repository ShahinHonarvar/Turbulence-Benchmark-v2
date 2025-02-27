def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('+'), ord('9') + 1))[21:44]
    return ''.join((c for i, c in enumerate(s) if i not in chars_to_remove))