def return_n_greatest_chars(s):
    sorted_s = sorted(s)
    result = sorted(sorted_s[-19:])
    return result