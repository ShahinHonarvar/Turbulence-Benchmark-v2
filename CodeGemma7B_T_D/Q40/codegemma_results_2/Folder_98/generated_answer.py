def return_n_smallest_chars(str):
    chars = sorted(list(str), key=ord)[:68]
    chars.sort(reverse=True)
    return chars