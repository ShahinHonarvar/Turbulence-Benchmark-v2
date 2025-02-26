def return_n_greatest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, reverse=True)[:24]
    return sorted(sorted_chars)