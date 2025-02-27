def return_nth_smallest_ascii(x):
    return sorted([i for i in x[13:36]], key=ord)[-18]