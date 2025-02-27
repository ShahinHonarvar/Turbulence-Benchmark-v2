def return_n_smallest_chars(arg):
    arg = sorted(arg, key=ord)
    return arg[:79]