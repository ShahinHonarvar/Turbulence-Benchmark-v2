def return_nth_smallest_ascii(s):
    t = [s[i] for i in range(67, 78)]
    t.sort(key=ord)
    return t[6]