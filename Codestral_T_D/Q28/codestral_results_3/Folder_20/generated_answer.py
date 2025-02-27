def return_nth_smallest_ascii(s):
    sub_s = s[25:65]
    sorted_chars = sorted(sub_s, key=ord)
    return sorted_chars[5]