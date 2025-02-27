def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[20:31]
    sub_str_sorted = sorted(sub_str)
    return sub_str_sorted[7]