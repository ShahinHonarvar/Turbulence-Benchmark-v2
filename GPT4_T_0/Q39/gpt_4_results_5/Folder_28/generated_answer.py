def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    greatest_chars = sorted_chars[:3]
    return sorted(greatest_chars)