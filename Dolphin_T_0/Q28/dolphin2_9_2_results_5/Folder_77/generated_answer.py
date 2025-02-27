def return_nth_smallest_ascii(s):
    sub = s[63:77]
    sorted_sub = sorted(sub, key=lambda x: ord(x))
    return sorted_sub[13]