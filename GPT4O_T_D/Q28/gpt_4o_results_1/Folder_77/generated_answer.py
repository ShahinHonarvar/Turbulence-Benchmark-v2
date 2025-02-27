def return_nth_smallest_ascii(s):
    sub_str = s[63:77]
    return sorted(sub_str)[13] if len(sub_str) >= 14 else None