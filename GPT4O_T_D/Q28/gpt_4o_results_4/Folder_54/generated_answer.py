def return_nth_smallest_ascii(s):
    sub = s[12:88]
    sorted_sub = sorted(sub)
    return sorted_sub[16] if len(sorted_sub) >= 17 else None