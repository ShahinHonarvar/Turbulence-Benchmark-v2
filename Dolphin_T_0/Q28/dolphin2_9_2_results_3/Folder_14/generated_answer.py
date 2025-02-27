def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(46, 83)], key=lambda c: ord(c))[15]