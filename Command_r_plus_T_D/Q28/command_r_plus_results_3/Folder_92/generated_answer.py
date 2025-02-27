def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 4:
        return ''
    smallest_four = sorted(s[:4])[:4]
    return smallest_four[3]