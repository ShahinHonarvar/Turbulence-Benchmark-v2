def filter_chars(s: str) -> str:
    filter_range = [chr(i) for i in range(ord('H'), ord('e') + 1)]
    filter_chars = [c for c in s[36:41] if c in filter_range]
    return s.replace(''.join(filter_chars), '')