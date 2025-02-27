def return_n_greatest_chars(s):
    return sorted([i for i in s], key=ord)[-2:]