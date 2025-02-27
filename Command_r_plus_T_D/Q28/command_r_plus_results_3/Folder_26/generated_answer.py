def return_nth_smallest_ascii(s: str) -> str:
    ascii_sorted = sorted(s[1:37], key=ord)
    return ascii_sorted[14]