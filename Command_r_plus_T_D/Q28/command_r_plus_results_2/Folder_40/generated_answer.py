def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[:5]
    ascii_sorted = sorted(sub_str)
    return ascii_sorted[4]