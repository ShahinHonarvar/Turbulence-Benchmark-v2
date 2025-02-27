def return_n_smallest_chars(str):
    a = sorted(str, key=ord)[:54]
    a.sort(reverse=True)
    return a