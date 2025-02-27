def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), key=ord, reverse=True)
    return sorted_chars[:35]