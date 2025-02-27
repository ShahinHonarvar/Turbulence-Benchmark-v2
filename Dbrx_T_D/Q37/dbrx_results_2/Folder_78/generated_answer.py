def filter_chars(s: str) -> str:
    chars_to_filter = set(s[75:100])
    chars_to_filter &= set(range(ord('8'), ord('f') + 1))
    return ''.join((c for c in s if c not in chars_to_filter))