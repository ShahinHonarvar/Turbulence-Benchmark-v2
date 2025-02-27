def return_nth_smallest_ascii(x):
    l = [ord(i) for i in x[20:81]]
    l.sort()
    return chr(l[10])