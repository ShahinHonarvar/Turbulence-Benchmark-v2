def return_nth_smallest_ascii(s: str) -> str:
    ascii_range = [chr(i) for i in range(32, 68)]
    ascii_set = set(s).intersection(ascii_range)
    ascii_sorted = sorted(ascii_set)
    return ascii_sorted[11] if len(ascii_sorted) > 11 else ''