def filter_chars(s: str) -> str:
    chars_to_remove = set(range(ord('*'), ord('s') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))