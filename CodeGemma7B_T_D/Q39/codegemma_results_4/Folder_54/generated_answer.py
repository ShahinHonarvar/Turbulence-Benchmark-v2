def return_n_greatest_chars(arg):
    return sorted(arg, key=ord, reverse=True)[:79]