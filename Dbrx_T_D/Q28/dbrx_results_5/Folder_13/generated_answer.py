def return_nth_smallest_ascii(s: str) -> str:
    chars_in_range = [c for c in s if 47 <= ord(c) <= 80]
    sorted_chars = sorted(chars_in_range)
    return sorted_chars[3]