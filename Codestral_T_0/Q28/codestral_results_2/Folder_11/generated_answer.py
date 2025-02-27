def return_nth_smallest_ascii(s):
    sub_s = s[9:60]
    sorted_chars = sorted(sub_s)
    return sorted_chars[5]