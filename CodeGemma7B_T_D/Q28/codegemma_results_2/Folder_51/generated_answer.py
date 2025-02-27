def return_nth_smallest_ascii(string):
    a = sorted(set(string))[1:10 + 1]
    return a[8]