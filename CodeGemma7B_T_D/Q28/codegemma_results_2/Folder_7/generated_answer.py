def return_nth_smallest_ascii(s):
    a = list(filter(lambda x: 12 <= s.index(x) <= 55, sorted(s)))
    return a[16]