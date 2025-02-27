def return_nth_smallest_ascii(s: str) -> str:
    chars = [c for c in s if 48 <= ord(c) <= 76]
    return sorted(chars)[4] if len(chars) > 5 else None