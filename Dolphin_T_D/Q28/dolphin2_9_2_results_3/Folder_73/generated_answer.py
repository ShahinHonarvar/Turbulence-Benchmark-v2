def return_nth_smallest_ascii(s):
    sub = s[0:70]
    return sorted(sub, key=lambda x: ord(x))[9]