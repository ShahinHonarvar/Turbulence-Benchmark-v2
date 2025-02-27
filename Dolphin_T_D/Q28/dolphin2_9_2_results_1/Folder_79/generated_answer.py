def return_nth_smallest_ascii(s):
    sub = s[13:36]
    return sorted(sub, key=ord)[17]