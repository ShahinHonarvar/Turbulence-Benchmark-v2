def return_nth_smallest_ascii(s: str) -> str:
    ascii_chars = [c for c in s if 58 <= ord(c) <= 85]
    chars_sorted = sorted(ascii_chars, key=ord)
    return chars_sorted[18]