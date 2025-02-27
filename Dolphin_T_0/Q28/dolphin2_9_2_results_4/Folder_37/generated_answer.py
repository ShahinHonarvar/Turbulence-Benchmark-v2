def return_nth_smallest_ascii(s):
    sub = s[28:68]
    sorted_sub = sorted(sub, key=lambda x: ord(x))
    return sorted_sub[14]