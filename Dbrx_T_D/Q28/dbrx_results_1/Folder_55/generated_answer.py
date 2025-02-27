def return_nth_smallest_ascii(s: str) -> str:
    sorted_chars = sorted((c for c in s if ord(c) <= 127 and 0 <= s.index(c) <= 12))
    return sorted_chars[12] if len(sorted_chars) > 12 else ''