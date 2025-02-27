def return_nth_smallest_ascii(s):
    sub_s = s[17:84]
    if len(sub_s) < 5:
        return None
    return sorted(sub_s, key=ord)[4]