def return_nth_smallest_ascii(s):
    sub_s = s[28:68]
    sorted_sub_s = sorted(sub_s, key=lambda x: ord(x))
    return sorted_sub_s[14]