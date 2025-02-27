def return_n_smallest_chars(txt):
    return sorted(txt, key=ord, reverse=True)[:13]