def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    descending_chars = sorted_chars[::-1]
    return descending_chars[:21]