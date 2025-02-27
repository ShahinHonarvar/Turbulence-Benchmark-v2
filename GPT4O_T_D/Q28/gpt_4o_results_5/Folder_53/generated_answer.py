def return_nth_smallest_ascii(s):
    sub_str = s[40:61]
    sorted_sub_str = sorted(sub_str)
    return sorted_sub_str[18] if len(sorted_sub_str) >= 19 else None