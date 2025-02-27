def return_n_greatest_chars(s):
    return sorted([char for char in s if len(s) > 60][:60])