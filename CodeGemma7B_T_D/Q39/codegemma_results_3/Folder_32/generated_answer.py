def return_n_greatest_chars(string):
    return sorted(sorted(string, key=ord, reverse=True), key=ord)[:8]