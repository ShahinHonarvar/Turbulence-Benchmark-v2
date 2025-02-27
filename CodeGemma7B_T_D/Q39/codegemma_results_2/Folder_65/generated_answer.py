def return_n_greatest_chars(input):
    return sorted(input, key=ord, reverse=True)[:27]