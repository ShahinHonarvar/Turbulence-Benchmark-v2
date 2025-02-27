def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[:5]
    ascii_sorted = sorted(sub_s, key=lambda x: ord(x))
    return ascii_sorted[3]