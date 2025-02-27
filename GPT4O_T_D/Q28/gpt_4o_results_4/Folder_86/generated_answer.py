def return_nth_smallest_ascii(s):
    sub_str = s[44:70]
    sorted_sub_str = sorted(sub_str, key=ord)
    return sorted_sub_str[14] if len(sorted_sub_str) >= 15 else None