def return_n_greatest_chars(st):
    return sorted(st, key=ord, reverse=True)[:85]