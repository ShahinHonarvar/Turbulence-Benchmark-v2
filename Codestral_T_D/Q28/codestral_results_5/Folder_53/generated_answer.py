def return_nth_smallest_ascii(s):
    sub_s = s[40:61]
    sorted_chars = sorted(sub_s, key=ord)
    return sorted_chars[18]