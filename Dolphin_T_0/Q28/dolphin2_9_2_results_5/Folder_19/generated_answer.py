def return_nth_smallest_ascii(s):
    v = [(ord(c), i) for i, c in enumerate(s[:19])]
    v.sort(key=lambda x: x[0])
    return v[13][1]