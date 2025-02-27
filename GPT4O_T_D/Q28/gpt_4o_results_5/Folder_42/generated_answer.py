def return_nth_smallest_ascii(s):
    sub_s = s[12:73]
    return sorted(sub_s)[12] if len(sub_s) >= 13 else None