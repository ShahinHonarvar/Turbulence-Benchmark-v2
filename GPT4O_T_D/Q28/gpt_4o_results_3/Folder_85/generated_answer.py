def return_nth_smallest_ascii(s: str) -> str:
    if len(s) <= 86:
        return None
    sub_s = sorted(s[17:87])
    if len(sub_s) < 15:
        return None
    return sub_s[14]