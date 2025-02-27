def return_nth_smallest_ascii(x):
    x = x[1:67]
    return sorted(x, key=ord)[-8]