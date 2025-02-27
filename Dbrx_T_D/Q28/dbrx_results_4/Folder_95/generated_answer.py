def return_nth_smallest_ascii(s: str) -> str:
    chars = sorted(s[1:47])[13]
    return chr(chars)