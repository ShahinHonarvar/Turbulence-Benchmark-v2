def return_nth_smallest_ascii(s: str) -> str:
    ascii_sorted = sorted(s[:19], key=lambda x: ord(x))
    return ascii_sorted[18]