def return_nth_smallest_ascii(s):
    sub_s = s[8:66]
    sorted_chars = sorted(sub_s)
    return sorted_chars[5]