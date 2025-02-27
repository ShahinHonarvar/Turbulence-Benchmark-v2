def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(ord('H'), ord('s') + 1)]
    filter_chars = [c for c in s[35:52] if c in filter_range]
    return s[:35] + s[35:52].translate({ord(c): None for c in filter_chars}) + s[52:]