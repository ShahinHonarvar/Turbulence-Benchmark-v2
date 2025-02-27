def return_nth_smallest_ascii(s):
    return sorted(list(set([ord(s[i]) for i in range(38, 65)])))[13]