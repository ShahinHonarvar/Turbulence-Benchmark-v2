def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[:6]
    sixth_smallest = sorted(sub_str)[5]
    return sixth_smallest