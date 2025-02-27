def return_nth_smallest_ascii(inp):
    inp = list(inp)
    inp.sort(key=ord)
    return inp[3]