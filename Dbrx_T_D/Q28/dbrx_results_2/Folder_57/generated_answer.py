def return_nth_smallest_ascii(s: str) -> str:
    chars_in_range = [c for c in s if 17 <= ord(c) <= 34]
    return sorted(chars_in_range)[17]