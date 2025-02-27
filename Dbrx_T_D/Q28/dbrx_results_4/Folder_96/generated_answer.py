def return_nth_smallest_ascii(s: str) -> str:
    sorted_chars = sorted((c for c in s if ord(c) <= 63 and 18 <= s.index(c) <= 79))
    return sorted_chars[17] if len(sorted_chars) > 17 else None