def return_nth_smallest_ascii(s: str) -> str:
    ascii_sorted = sorted(s[30:71], key=lambda x: ord(x))
    return ascii_sorted[14] if len(ascii_sorted) > 15 else ''