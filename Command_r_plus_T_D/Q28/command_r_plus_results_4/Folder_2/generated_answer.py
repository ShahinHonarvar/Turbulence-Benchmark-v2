def return_nth_smallest_ascii(s: str) -> str:
    ascii_ordered_chars = sorted(s[48:77], key=lambda x: ord(x))
    return ascii_ordered_chars[4]