def return_n_greatest_chars(s):
    sorted_s = sorted(s)
    greatest_chars = sorted_s[-34:]
    return sorted(greatest_chars)