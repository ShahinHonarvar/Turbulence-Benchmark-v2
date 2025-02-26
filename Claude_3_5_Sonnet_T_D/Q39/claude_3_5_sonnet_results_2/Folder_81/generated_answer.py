def return_n_greatest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)
    return sorted(sorted_chars[:64])