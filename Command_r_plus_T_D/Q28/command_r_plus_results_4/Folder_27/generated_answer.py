def return_nth_smallest_ascii(s: str) -> str:
    ascii_range = [chr(i) for i in range(33, 86)]
    ascii_in_range = [c for c in s if c in ascii_range]
    ascii_in_range.sort()
    return ascii_in_range[12] if len(ascii_in_range) > 12 else ''