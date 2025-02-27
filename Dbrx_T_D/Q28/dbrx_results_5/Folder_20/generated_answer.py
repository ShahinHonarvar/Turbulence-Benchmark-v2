def return_nth_smallest_ascii(s: str) -> str:
    chars = sorted(set(s[24:65]))
    return chars[5] if len(chars) > 5 else None