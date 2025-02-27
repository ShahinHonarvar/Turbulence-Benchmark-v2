import string

def return_nth_smallest_ascii(s):
    sub_s = s[25:65]
    return min(sub_s, key=ord)