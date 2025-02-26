def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), reverse=True)[:45]
    return sorted(sorted_chars)