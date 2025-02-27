def return_nth_smallest_ascii(s):
    sub_string = s[29:48]
    return sorted(sub_string)[6] if len(sub_string) >= 7 else None