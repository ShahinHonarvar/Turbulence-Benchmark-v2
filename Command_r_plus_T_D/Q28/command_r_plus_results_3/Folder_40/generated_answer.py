def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[:5]
    sorted_sub_s = sorted(sub_s)
    return sorted_sub_s[4]