def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[25:65]
    sixth_smallest_ascii = sorted(sub_s)[5]
    return sixth_smallest_ascii