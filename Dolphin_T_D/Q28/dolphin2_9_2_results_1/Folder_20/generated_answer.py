def return_nth_smallest_ascii(in_str: str) -> str:
    lst = in_str[25:65]
    return sorted(lst, key=lambda x: ord(x))[5]