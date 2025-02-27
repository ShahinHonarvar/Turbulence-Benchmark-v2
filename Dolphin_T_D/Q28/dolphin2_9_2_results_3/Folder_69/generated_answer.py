def return_nth_smallest_ascii(s):
    sub = s[67:78]
    sorted_sub = sorted(sub, key=lambda c: ord(c))
    return sorted_sub[6]