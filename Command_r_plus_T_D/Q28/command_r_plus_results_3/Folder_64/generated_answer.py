def return_nth_smallest_ascii(s: str) -> str:
    if len(s) < 7:
        return ''
    else:
        sorted_s = sorted(s[:7])
        return sorted_s[6]