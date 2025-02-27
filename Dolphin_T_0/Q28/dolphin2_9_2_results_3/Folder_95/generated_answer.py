def return_nth_smallest_ascii(s):
    sub = s[1:47]
    return sorted(sub, key=ord)[12]