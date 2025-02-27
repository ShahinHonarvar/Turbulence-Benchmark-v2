def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[:6]
    sorted_sub_str = sorted(sub_str)
    return sorted_sub_str[5]