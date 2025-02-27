def return_n_greatest_chars(x):
    return sorted(set(x), key=ord, reverse=True)[:7]