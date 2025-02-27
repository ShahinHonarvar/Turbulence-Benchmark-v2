def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars))[-76:]
    return sorted_chars