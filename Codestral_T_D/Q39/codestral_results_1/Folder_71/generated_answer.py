def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True)
    greatest_chars = sorted_chars[:14]
    sorted_greatest_chars = sorted(greatest_chars)
    return sorted_greatest_chars