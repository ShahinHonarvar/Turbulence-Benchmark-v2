def return_nth_smallest_ascii(s: str) -> str:
    smallest_five = sorted(s[:5])[:5]
    return smallest_five[4]