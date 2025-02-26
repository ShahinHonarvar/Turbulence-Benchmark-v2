def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=ord, reverse=True)[:28]
    return sorted_chars