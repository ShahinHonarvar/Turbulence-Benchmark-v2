def return_nth_smallest_ascii(s: str) -> str:
    sub_str = s[47:81]
    ascii_sorted = sorted(sub_str, key=lambda x: ord(x))
    return ascii_sorted[3]