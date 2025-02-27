def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 12:
        return ''
    else:
        s = s[:12]
        return min(s, key=ord)