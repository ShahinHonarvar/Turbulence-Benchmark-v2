def return_n_greatest_chars(string):
    unique_chars = set(string)
    sorted_chars = sorted(unique_chars, reverse=True)
    return sorted_chars[:26]