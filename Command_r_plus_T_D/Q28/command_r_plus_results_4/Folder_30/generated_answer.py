def return_nth_smallest_ascii(s: str) -> str:
    ascii_ordered = sorted(s[50:77], key=lambda x: ord(x))
    return ascii_ordered[10]