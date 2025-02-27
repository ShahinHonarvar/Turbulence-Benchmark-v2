def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[15:22]
    sixth_smallest_ascii = sorted(sub_str)[5]
    return sixth_smallest_ascii