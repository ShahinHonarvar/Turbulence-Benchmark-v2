def return_nth_smallest_ascii(s):
    sub_s = s[37:60]
    sorted_chars = sorted(sub_s, key=ord)
    return sorted_chars[5]