def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[25:65]
    sub_s_sorted = sorted(sub_s)
    return sub_s_sorted[5]