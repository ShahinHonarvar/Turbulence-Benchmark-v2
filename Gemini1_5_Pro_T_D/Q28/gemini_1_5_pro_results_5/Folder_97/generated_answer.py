def return_nth_smallest_ascii(s):
    return sorted(list(set([ord(x) for x in s[15:22]])))[5]