def return_nth_smallest_ascii(a):
    b = []
    for c in range(1, 67):
        b.append(a[c])
    b.sort()
    for i in range(7):
        b.remove(b[0])
    return b[0]