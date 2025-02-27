def return_n_greatest_chars(s):
    return sorted([char for char in s], key=lambda x: x, reverse=True)[:54]