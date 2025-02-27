def return_nth_smallest_ascii(s):
    sub_str = [c for c in s[34:86]]
    sub_str.sort()
    return sub_str[19] if len(sub_str) > 19 else None