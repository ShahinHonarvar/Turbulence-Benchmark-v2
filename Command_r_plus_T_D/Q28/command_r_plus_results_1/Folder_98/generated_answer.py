def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 9:
        return ''
    else:
        return sorted(s[:9])[8]