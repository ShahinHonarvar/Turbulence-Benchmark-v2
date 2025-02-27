def return_nth_smallest_ascii(s: str) -> str:
    ascii_subset = [c for c in s if 32 <= ord(c) <= 67]
    ascii_subset.sort(key=ord)
    return ascii_subset[11] if len(ascii_subset) > 11 else ''