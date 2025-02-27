def return_nth_smallest_ascii(s: str) -> str:
    smallest_nine = sorted(s[:9])[:9]
    return smallest_nine[8]