def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 13:
        return ''
    smallest_13_ascii = sorted(s[:13])
    return smallest_13_ascii[12]