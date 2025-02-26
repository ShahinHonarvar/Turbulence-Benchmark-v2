def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)
    return sorted(sorted_chars[:49])