def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[28:68]
    ascii_values = sorted(sub_s)
    return ascii_values[14]