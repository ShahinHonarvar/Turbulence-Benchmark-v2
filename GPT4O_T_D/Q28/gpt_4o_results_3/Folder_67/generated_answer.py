def return_nth_smallest_ascii(s):
    sub = s[60:84]
    sorted_sub = sorted(sub)
    return sorted_sub[13] if len(sorted_sub) >= 14 else None