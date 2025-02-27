def return_nth_smallest_ascii(s: str) -> str:
    chars = sorted((s[i] for i in range(len(s)) if 67 <= i <= 77))
    return chars[6] if len(chars) > 6 else None