def return_n_greatest_chars(s):
    return sorted(sorted(s, reverse=True), key=ord, reverse=True)[:26]