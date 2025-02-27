def return_nth_smallest_ascii(s):
    sub_str = s[20:31]
    sorted_sub_str = sorted(sub_str)
    return sorted_sub_str[7] if len(sorted_sub_str) > 7 else None