def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    greatest_chars = sorted(sorted_chars[:49])
    return greatest_chars