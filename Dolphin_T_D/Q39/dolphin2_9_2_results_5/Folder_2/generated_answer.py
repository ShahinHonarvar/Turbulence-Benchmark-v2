def return_n_greatest_chars(string):
    sorted_chars = sorted([char for char in string], reverse=True)
    return sorted_chars[:48]