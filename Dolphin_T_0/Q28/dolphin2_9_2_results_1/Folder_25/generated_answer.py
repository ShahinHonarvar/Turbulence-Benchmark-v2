def return_nth_smallest_ascii(s):
    sub_s = s[34:69]
    sorted_sub_s = sorted(sub_s, key=lambda c: ord(c))
    return sorted_sub_s[5]